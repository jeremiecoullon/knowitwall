$(window.vent).on('showViewerCompleted', function() {
      // To parse the annotation, we've tried 3 different things so far.

      // Parses message as html, and passes it back to the annotation
      var text = $('.annotator-annotation div').text();
      // var knowit_title = "<img src='/static/Images/know-it.png' class='knowit_img'>"
      $('.annotator-annotation div').html(text);

      // Explanator text expands on click:
      $('#annotator-question_mark').click(function (){
        var elem_display = $('#knowit_explanation').css('display');
        if (elem_display === 'none'){
          $('#knowit_explanation').css('display','block')
        }
        else if (elem_display === 'block'){
          $('#knowit_explanation').css('display','none')
        }
      })
    });
