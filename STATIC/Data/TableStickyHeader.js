$(document).ready(function(){
    $(".sticky-header").floatThead();
    $(".clickable-row").click(function() {
        window.location = $(this).data("href");
    });
});