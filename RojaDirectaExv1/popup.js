// Copyright (c) 2012 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.
/*
$.get("http://www.joindota.com/en/start", function(data){
  var mainDiv = $("#matchticker", data); // finds <div id='mainDiv'>...</div>
}, "html");
$("#gg").load("http://www.joindota.com/en/start #mainDiv");

$.ajax({
    url: 'http://www.joindota.com/en/start',
    type: 'GET',
    success: function(res) {
        //console.log(res);
        var aux  = $(res.responseText).find("#matchticker");
        console.log($(aux).html());
        //$(aux).appendTo('body');
        $("body").append($(aux).html());
        
    }
});*/
/*
var xhr = new XMLHttpRequest();
var url = "http://www.joindota.com/en/start ";
xhr.open('GET', url, true);
xhr.onload = ff;
xhr.send();

function ff(){
     //var photos = xhr.responseXML.getElementById("#matchticker");
     var photos = xhr.responseXML.find('#matchticker');
     console.log("a");
     
}
*/


// Or create an HTML notification:
//var notification = webkitNotifications.createHTMLNotification(
  //'notification.html'  // html url - can be relative
//);
function crearXMLHttpRequest() 
  {
    var xmlHttp=null;
    if (window.ActiveXObject) 
      xmlHttp = new ActiveXObject("Microsoft.XMLHTTP");
    else 
      if (window.XMLHttpRequest) 
        xmlHttp = new XMLHttpRequest();
    return xmlHttp;
  }

function procesarEventos()
  {
    
    if(conexion.readyState == 4)
    {
      //esta linea par el json
      //var objecto=eval('(' + conexion.responseText + ')');
      var notification = webkitNotifications.createNotification( '48.png', 'FF', 'llamada ajax'  );
      notification.show();  
      //console.log("ds");      
    } 
    else 
    {
      console.log("cargando");
    }
  }

var conexion;
var url = 'http://localhost:8085/';
setInterval(function() {
  

  //console.log("ants");
  conexion=crearXMLHttpRequest();
  conexion.onload = procesarEventos;
  conexion.open('GET',url,true);
  conexion.send();

},5000);


// Then show the notification.
