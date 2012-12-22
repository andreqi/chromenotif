#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import json
import urllib2
import BeautifulSoup

form ="""
<html>
<head></head>
<body>
%(valor)s
</body>
<label> fuentes </label>
</html>
"""



class MainHandler(webapp2.RequestHandler):	

    def get(self):
        f = urllib2.urlopen('http://www.rojadirecta.me/')
        resultado = self.obtenerJson(f.read())

        self.response.write( resultado )

    def obtenerJson (self,data):
        soup = BeautifulSoup.BeautifulSoup(data) 
        prueba = soup.find("div", {"id": "agendadiv"})
        result = form % {"valor": prueba}
        #cadena={"c": 3, "e": 2, "a": 1}
        cadena = [ { "tipo" : "Basquet" , "hora" : "4:00" , "team1" : "Peru" , "team2" : "Chile"} , { "tipo" : "Futbol" , "hora" : "8:00" , "team1" : "Argentina" , "team2" : "Brasil"},
                 { "tipo" : "Golf" , "hora" : "7:00" , "team1" : "Ecuador" , "team2" : "EEUU"}]
        #cadena = [ {"a":0,"b":1},{"a":3,"b":4},{"a":5,"b":6} ]
        return json.dumps(cadena)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True) 
