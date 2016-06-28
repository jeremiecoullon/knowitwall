// Filter disciplines in the archive page. On each button click:
// 1. Add yellow background-color
// 2. Remove yellow background-color for other buttons
// 3. Display/hide relevant episodes
// 4. Remove padding-bottom from the last episode in the selected list

var archive_filter = function(){
  // the last box shouldn't have padding-bottom by default
  $('.archive_image_padding:last').css('padding-bottom','0px');

  $('#button_All').click(function(){
    $('#button_All').css({"background-color": "rgba(255, 194, 28, 0.8)", "border-radius": "7px"})
    $('#button_Arts').css({"background-color": ""})
    $('#button_Sciences').css({"background-color": ""})

    $('#archive_category').html('All Episodes');
    $('.archive_episode_category_Arts').css('display','inline');
    $('.archive_episode_category_Sciences').css('display','inline');

    // return padding-bottom to it's default setting (4px) when you click on 'All'
    // remove padding from the bottom of the last episode in the list
    $('.archive_episode_category_Sciences:last .archive_image_padding').css('padding-bottom','');
    $('.archive_episode_category_Arts:last .archive_image_padding').css('padding-bottom','');
    $('.archive_image_padding:last').css('padding-bottom','0px');
  });

  $('#button_Arts').click(function(){
    $('#button_All').css({"background-color": "rgba(255, 194, 28, 0)"})
    $('#button_Arts').css({"background-color": "rgba(255, 194, 28, 0.8)", "border-radius": "7px"})
    $('#button_Sciences').css({"background-color": ""})

    $('#archive_category').html('Arts');
    $('.archive_episode_category_Arts').css('display','inline');
    $('.archive_episode_category_Sciences').css('display','none');

    $('.archive_episode_category_Arts:last .archive_image_padding').css('padding-bottom','0px');

  });

  $('#button_Sciences').click(function(){
    $('#button_All').css({"background-color": "rgba(255, 194, 28, 0)"})
    $('#button_Arts').css({"background-color": ""})
    $('#button_Sciences').css({"background-color": "rgba(255, 194, 28, 0.8)", "border-radius": "7px"})

    $('#archive_category').html('Sciences');
    $('.archive_episode_category_Sciences').css('display','inline');
    $('.archive_episode_category_Arts').css('display','none');

    $('.archive_episode_category_Sciences:last .archive_image_padding').css('padding-bottom','0px');
  });
}
archive_filter();
