function notificar(response){
	//if (response.notificar){
		var notification = webkitNotifications.createNotification('48.png','Partido siguiente',  response );
		notification.show();
		console.log("ds");
  //}
}

setInterval(function() {
  console.log("ants");
  $.ajax({
    url: 'http://localhost:8085/',
    type: 'GET',
    success: function(res) {
        //console.log(res); 
        //notificar("llego info")
        var notification = webkitNotifications.createNotification('icon.png','Partido siguiente',  response );
        notification.show();
        console.log("ds");
        } 
    });
},3000);