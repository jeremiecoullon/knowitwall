var scrollAmount = 95;

$(window).on('scroll', function(){
  if($(window).scrollTop()>=scrollAmount && !$('nav').hasClass('fixed')){
    $('nav').addClass('fixed');
  }

});
