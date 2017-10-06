function faceMove(){
    var number = Math.floor(Math.random() * 101);
    var div = $(".my-face");
    div.animate({left: number + "%"}, 2000);
    div.animate({top: number + "%"}, 2000, faceMove);
  }

$( document ).ready(function() {
    var windowWidth = $(window).width();
    if(windowWidth < 600){
      $('#portfolio').click(function() {
          $('.body-container').css("margin-top", "10px")
          $('.body-container2').slideToggle(1000)
      })
      $('.upbutton').click(function() {
          $('.body-container').css("margin-top", "10px")
           $('.body-container2').slideUp(1000);
      })
      $('.fa-bars').click(function(){
        $('.nav-links').slideToggle(1000);
      })
    }

    if (windowWidth >= 601 ){
      $('#portfolio').click(function() {
          $('.body-container1').slideToggle(1000);
      })
      $('.upbutton').click(function() {
           $('.body-container1').slideUp(1000);
      })
    }

faceMove()

  $('.sendbutton').mouseover(function() {
      $(this).css({'border':'#363531 4px solid','color':'#6b6d70','background-color':'black'});
  })
  $('.sendbutton').mouseleave(function() {
    $(this).css({'border':'#363531 4px solid','color':'#6b6d70','background-color':'#dde0db'});
  })

})
