$("form[name=register_form]").submit(function (e) {
  e.preventDefault();

  var $form = $(this);
  var $error = $form.find(".error");
  var $success = $form.find(".success");
  var data = $form.serialize();

  $.ajax({
    url: "/register",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (resp) {
      console.log("Register Success:", resp);
      if (resp.success) {
        $success.text(resp.success).removeClass("error--hidden").show();
        $error.hide();
        $form[0].reset(); 
      }
    },
    error: function (resp) {
      console.log("Register Error:", resp);   
      if (resp.responseJSON && resp.responseJSON.error) {
        $error.text(resp.responseJSON.error).removeClass("error--hidden").show();
        $success.hide();
      } else {
        $error.text("Terjadi kesalahan").removeClass("error--hidden").show();
        $success.hide();
      }
    },
  });
});

$("form[name=login_form]").submit(function (e) {
  e.preventDefault();

  var $form = $(this);
  var $error = $form.find(".error");
  var data = $form.serialize();

  $.ajax({
    url: "/login",
    type: "POST",
    data: data,
    dataType: "json",
    success: function (resp) {
      console.log("Login Success:", resp);
      if (resp.success) {
        $success.text(resp.success).removeClass("error--hidden").show();
        $error.hide();
      }
      window.location.href = "/home";
    },
    error: function (resp) {
      console.log("Login Error:", resp);  
      if (resp.responseJSON && resp.responseJSON.error) {
        $error.text(resp.responseJSON.error).removeClass("error--hidden").show();
      } else {
        $error.text("Terjadi kesalahan saat login").removeClass("error--hidden").show();
      }
    },
  });
});
