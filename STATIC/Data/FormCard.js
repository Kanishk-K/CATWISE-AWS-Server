$(document).ready(function () {
  $('#form_tabs a').on('click', function (e) {
    e.preventDefault()
    $(this).tab('show')
  })
  $('.datepicker').datepicker({
    format: "yyyy-mm-dd",
    todayBtn: "linked",
    orientation: "top right",
    todayHighlight: true
  });
  $('#check').on("click", function(){
    let valid = true;
    $('[required]').each(function() {
      if ($(this).is(':invalid') || !$(this).val()) valid = false;
    })
    if (!valid){
      $(document.body).append(
        `
        <div class="alert show bg-warning d-none d-md-flex">
          <span class="fas fa-upload ICON text-white"></span>
          <span class="msg text-white">Not all required fields are filled.</span>
          <div class="close-btn bg-warning">
              <span class="fas fa-times text-white"></span>
          </div>
        </div>
        `
      )
      $('.alert').addClass("showAlert");
      setTimeout(function(){
        $('.alert').removeClass("show");
        $('.alert').remove();
      },5000);
      $('.close-btn').click(function(){
          $('.alert').removeClass("show");
          $('.alert').remove();
      });
    }
  })
});