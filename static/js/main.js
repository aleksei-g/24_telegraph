$(function(){
  if (window.location.pathname == '/') {
    EditArticle()
  }
  else {
    ShowArticle()
  };
});

$("#postForm").submit(function(event) {
  event.preventDefault();
  $.ajax({
    url: '/save/'+$('form').find( 'input[name="author_id"]' ).val( ),
    type: 'POST',
    dataType: 'json',
    data: $('form').serialize(),
    success: function(response) {
      history.pushState(null, null, response.article_id);
      document.title = response.header + ' / '+ response.title;
      $('form').find( 'input[name="author_id"]' ).val( response.article_id );
      $("#postForm").hide();
      $("#result").show();
      $( "div#result .header" ).html( response.header );
      $( "div#result .signature" ).html( response.signature );
      $( "div#result .article" ).html( response.body );
      if (response.author == true) {
        $("div#result .edit-btn").show();
      };
    },
  });
});

function EditArticle(){
  $("#postForm").show();
  $("#result").hide();
};

function ShowArticle(){
  $("#postForm").hide();
  $("#result").show();
  if ( author == "True" ) {
    $("div#result .edit-btn").show();
  }
  else {
    $("div#result .edit-btn").hide();
  };
};