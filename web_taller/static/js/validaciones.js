$(function(){

    $("#formulario").validate({

        //reglas que se deben cumplir y mensajes a enviar
        rules:{
            txtPatente:{
                required: true,
                maxlength: 7
            },

        },
        messages:{
            txtPatente:{
                required: "la patente es obligatoria",
                maxlength: "La patente debe tener 7 caracteres"
            },
            txtAnnio:{
                required: "el año es obligatorio",
                number: "ingrese solo números"
            }
        },
        errorClass: "color-rojo",
        validClass: "color-verde"
        
    });

});

