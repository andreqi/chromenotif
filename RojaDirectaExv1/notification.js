function procesarEventos()
  {
    
    if(conexion.readyState == 4)
    {
        var matches = JSON.parse(conexion.responseText);
        for (var i=0; i<matches.length;i++){
          //console.log(" i "+i+" match a " + matches[i].a +" b "+matches[i].b);
          var notification = webkitNotifications.createNotification( '48.png' , matches[i].tipo + " Hora " +matches[i].hora,
            matches[i].team1 + " vs " + matches[i].team2+"<a href='www.google.com'>" );
            /*var notification = webkitNotifications.createHTMLNotification(
              'popup.html'  // html url - can be relative
            );*/
            notification.show();
        }
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
  conexion=new XMLHttpRequest();
  conexion.onload = procesarEventos;
  conexion.open('GET',url,true);
  conexion.send();

},5000);


// Then show the notification.
