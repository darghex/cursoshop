/*
  document.getElementById("btnGuardar").onclick = function (){
    var txts = document.getElementsByName("txtNota");
    var size = txts.length - 1;
    var acum = 0;
    for ( var i = 0; i <= size; i++){
      acum = acum + parseInt(txts[i].value);
    }
    console.log("Promedio: "+ acum / size);
  }

  */



  $(document).ready( function (){
        //garantizamos que el DOM esta full loaded
        $('#btnGuardar').click( calcular2 );
        // codificar todo aquello de los elementos del DOM

  });

      function calcular() {
          var acum = 0;
          $("input.txtNota").each( function ( index, element){
             acum = acum + parseInt($(element).val()) ;
          } );
          console.log("Promedio: "+ acum / $("input.txtNota").length);
        }


        function calcular2() {
          var txts = $("input.txtNota");
          var size = txts.length - 1;
          var acum = 0;
          for ( var i = 0; i <= size; i++){
            acum = acum + parseInt(txts[i].value);
          }
          console.log("Promedio: "+ acum / size);
        }
