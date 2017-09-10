$( document ).ready(function() {
    var windowWidth = $(window).width();
    if(windowWidth < 600){
      $('#portfolio').click(function() {
          $('.body-container').css("margin-top", "10px")
          $('.body-container2').slideToggle(1000)
      })
      $('.upbutton').click(function() {
          $('.body-container').css("margin-top", "130px")
           $('.body-container2').slideUp(1000);
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


  $('.sendbutton').mouseover(function() {
      $(this).css({'border':'#363531 4px solid','color':'#6b6d70','background-color':'black'});
  })
  $('.sendbutton').mouseleave(function() {
    $(this).css({'border':'#363531 4px solid','color':'#6b6d70','background-color':'#dde0db'});
  })
})
