
  function reprobado(vUrl) {

    $.ajax({
      url: vUrl,
      type:'GET',
      datatype:'json',
      success: function (data) {
        ul = document.getElementById("reprobado");
        btn = document.getElementById("btnvolver");
        text= ""
        for (a in data){
          text = text + "<li class='collection-item avatar'><a href='/alumno/" + data[a].id + "/detail/'><img src='../../media/" + data[a].foto + "' class='circle'><span class='title'></a><a href='/alumno/" + data[a].id + "/detail/''>" + data[a].nombre + "</a></span><p>" + data[a].cedula + "</p><div class='content-action'><a href='/alumno/" + data[a].id + "/detail/'><i class='material-icons' title='detalles'>details</i></a><a class='delete' href='/alumno/" + data[a].id + "/delete/'><i class='material-icons' title='eliminar'>delete_forever</i></a></div></li>";
        }
        ul.innerHTML = text;
        btn.classList.remove("hide");
      }

    });


};


function notificacion(id) {
  $.ajax({
    data : { 'id': id },
    url: 'listall',
    type:'GET',
    success: function(data) {
        if(data!=""){
          alert("solicitud nueva");
          window.location.reload()
        }
        setTimeout(function (){ notificacion(id); }, 1000 *60);
      }
    });

}
