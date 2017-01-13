function SendForm(){
  $.ajax({
    url: '/save/'+articleID,
    type: 'POST',
    dataType: 'json',
    data: $('form').serialize(),
    success: function(response){
      document.cookie = response.cookie_str;
      window.location.pathname = response.path;
    },
  });
};