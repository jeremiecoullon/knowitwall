$(window.vent).on('showViewerCompleted', function() {
    // hide annotation if the mouse is over the annotation
    $('.annotator-viewer').css('display','none');

    // Force show current annotation if highlight clicked on.
    var toggledOnce = false;
    $('.annotator-hl').click(function () {
        if (toggledOnce) {
            return;
        }
        // $('.audiodoc_page_box').animate({'margin-left': '5%'}, 'slow');
        $('.audiodoc_page_box').toggleClass('audiodoc_page_box_knowit');
        $('.annotator-viewer').toggleClass('annotator-viewer_show');
        toggledOnce = true;
    });

    // The 'close' button on annotation hides it
    $('.annotator-close').click(function () {
        $('.audiodoc_page_box').toggleClass('audiodoc_page_box_knowit');
        $('.annotator-viewer').toggleClass('annotator-viewer_show');
        toggledOnce = true;
    });

    // To parse the annotation, we've tried 3 different things so far.

    // 1. parses message as html
    var text = $('.annotator-annotation div').text();

    var knowit_title = "<img src='/static/Images/KIW_logo_circle.png' style='width:50px;margin-left:42%;'>"
    $('.annotator-annotation div').html(knowit_title+text);
    // -----------------------

    // 2. Find and replace text URLs into hyperlinks.
    // var text = $('.annotator-annotation div').text();
    // var regex = /(https?:\/\/([-\w\.]+)+(:\d+)?(\/([-\w\/_\.]*(\?\S+)?)?)?)/ig
    // var replaced_text = text.replace(regex, "<a href='$1' target='_blank'>$1</a>");
    // $('.annotator-annotation div').html(replaced_text);

    // -----------------------

    // 3. assume the text is exactly a URL and pass it to crossdomain
    // var request = $.ajax({
    //     type: 'GET',
    //     url: 'http://localhost:5000/crossdomain',
    //     data: {url:text}
    // });
    // request.done(function(reply){
    //   // replaced_text = text.replace(text,JSON.stringify(reply))
    //   var replaced_text = reply
    //   $('.annotator-annotation div').html(replaced_text);
    // });
});


// This acts weirdly
// $(window.vent).on('showViewerCompleted', function() {
//   var oddClick = true;
//   $(".annotator-hl").click(function() {
//     $('.audiodoc_page_box').animate({'margin-left': oddClick ? '5%': '20%'}, 'slow');
//       oddClick = !oddClick;
//   });
// });
