$(document).ready(function(){
    // Show Initial Properties of CatWises
    $(".ID").show();
    $('#ID').prop('checked', true);
    $(".RA").show();
    $('#RA').prop('checked', true);
    $(".DEC").show();
    $('#DEC').prop('checked', true);
    $(".W1mpro").show();
    $('#W1mpro').prop('checked', true);
    $(".W2mpro").show();
    $('#W2mpro').prop('checked', true);
    $("input:checkbox").each(function(){
        $(this).change(function(){
            var colName = $(this).data("column");
            if (this.checked){
                $('.'+colName).show();
            }
            else{
                $('.'+colName).hide();
            }
        })
    });
    $(".sticky-header").floatThead();
    $("#collapse-example,#collapse-columns").each(function(){
        $(this).on('shown.bs.collapse hidden.bs.collapse', function(){
            $(".sticky-header").floatThead('reflow');
        })
    })
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});