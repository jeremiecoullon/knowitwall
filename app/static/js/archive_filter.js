// Filter disciplines in the archive page. On each button click:
// 1. Add yellow background-color
// 2. Remove yellow background-color for other buttons
// 3. Display/hide relevant episodes
var archive_filter = function(){

  $('#button_All').click(function(){
    $('#button_All').css({"background-color": "rgba(255, 194, 28, 0.8)", "border-radius": "7px"})
    $('#button_Arts').css({"background-color": ""})
    $('#button_Sciences').css({"background-color": ""})

    $('#archive_category').html('All Episodes');
    $('.archive_episode_category_Arts').css('display','inline');
  $('.archive_episode_category_Sciences').css('display','inline');
  });

  $('#button_Arts').click(function(){
    $('#button_All').css({"background-color": "rgba(255, 194, 28, 0)"})
    $('#button_Arts').css({"background-color": "rgba(255, 194, 28, 0.8)", "border-radius": "7px"})
    $('#button_Sciences').css({"background-color": ""})

    $('#archive_category').html('Arts');
    $('.archive_episode_category_Arts').css('display','inline');
    $('.archive_episode_category_Sciences').css('display','none');
  });

  $('#button_Sciences').click(function(){
    $('#button_All').css({"background-color": "rgba(255, 194, 28, 0)"})
    $('#button_Arts').css({"background-color": ""})
    $('#button_Sciences').css({"background-color": "rgba(255, 194, 28, 0.8)", "border-radius": "7px"})

    $('#archive_category').html('Sciences');
    $('.archive_episode_category_Sciences').css('display','inline');
    $('.archive_episode_category_Arts').css('display','none');
  });
}
archive_filter();
