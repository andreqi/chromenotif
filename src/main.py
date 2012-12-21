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
        return result

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
