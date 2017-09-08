$( document ).ready(function() {
    $('#portfolio').click(function() {
        $('.body-container1').slideToggle(1000);
    })
    $('.upbutton').click(function() {
         $('.body-container1').slideUp(1000);
    })
    $('.sendbutton').mouseover(function() {
        $(this).addClass("Animate");
        $(this).css({'border':'black 1px solid','color':'#6b6d70','background-color':'black'});
    })
    $('.sendbutton').mouseleave(function() {
      $(this).removeClass("Animate",1000);
      $(this).css({'border':'none','color':'#6b6d70','background-color':'#dde0db'});
    })
})
