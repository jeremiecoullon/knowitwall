// filter disciplines in the archive page
var archive_filter = function(){

  $('#button_All').click(function(){
    $('#archive_category').html('All Episodes');
    $('.archive_episode_category_Arts').css('display','inline');
  $('.archive_episode_category_Sciences').css('display','inline');
  });

$('#button_Arts').click(function(){
  $('#archive_category').html('Arts');
  $('.archive_episode_category_Arts').css('display','inline');
$('.archive_episode_category_Sciences').css('display','none');
});

$('#button_Sciences').click(function(){
  $('#archive_category').html('Sciences');
  $('.archive_episode_category_Sciences').css('display','inline');
$('.archive_episode_category_Arts').css('display','none');
});

}
archive_filter();


// Version 1: creating categories client-side
// Click on 'Arts' button:
// 1. check toggle_variable: if toggle_variable === 'Arts': do nothing. Else, continue
// 3. get list of all disciplines in hidden div (or json)
// 4. If isNotInCategory returns true: build list of css classes with those disciplines
// 5. Build list of css classes for the 'Arts'
// 5. apply 'display: none;' to non-'Arts' discplines. apply 'display:inline;' to 'Arts'


// Version 2: create categories server side (in json)
// click on 'Art':
// 1. check toggle_variable: if toggle_variable === 'Arts': do nothing. Else, continue
// 2. apply 'display: none;' to all non-Arts categories. apply 'display: inline' to 'Arts'

// Click on 'All':
// check toggle_variable. if already on 'All': do nothing
// apply 'display:inline;' to all categories
