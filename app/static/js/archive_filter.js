// filter disciplines in the archive page
var archive_filter = function(){

  // Arrays of episode discplines in each category
  var Arts_list = ['Italian Literature', 'History', 'History of Science', 'Linguistics', 'English Literature', 'Philosophy'];
  var Sciences_list = ['Physics', 'Neuroscience', 'Geography', 'Biology', 'Earth Science', 'Palaeontology', 'Astrophysics'];

// Checks whether episode is NOT within a category or not.
// Returns true if it isn't; false if it is.
  function isNotInCategory(value,array){
    return ~array.indexOf(value) >-1;
  }
console.log(isNotInCategory('History',Arts_list));


}
archive_filter();


// TODO:
// python passes list of all disciplines
// archive_filter.js gets that array: loops through it and returns true or false
// if true: insert css: "display:none;". if false, do nothing
