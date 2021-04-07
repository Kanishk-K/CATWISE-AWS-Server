$("#delete-check").on('input', function () {
    if ($("#delete-check").val() == $("#delete-check").data('correctval')){
        $("#delete-button").prop("disabled",false);
    }
    else{
        $("#delete-button").prop("disabled",true);
    }
});