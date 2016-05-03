$(window.vent).on('showViewerCompleted', function() {
    // hide annotation if the mouse is over the annotation
    // $('.annotator-viewer').css('display','none');

    // Force show current annotation if highlight clicked on.
    // var toggledOnce = false;
    // $('.knowit_button').click(function () {
    //     if (toggledOnce) {
    //         return;
    //     }
    //     $('.annotator-viewer').toggleClass('annotator-viewer_show');
    //     toggledOnce = true;
    // });
    //
    // // The 'close' button on annotation hides it
    // $('.annotator-close').click(function () {
    //     $('.annotator-viewer').toggleClass('annotator-viewer_show');
    //     toggledOnce = true;
    // });
    // To parse the annotation, we've tried 3 different things so far.

    // 1. parses message as html
    var text = $('.annotator-annotation div').text();

    var knowit_title = "<img src='/static/Images/know-it.png' style='width:125px;margin-left:41.5%;border:1px solid #2c3e50; border-radius:10px;padding:7px;margin-bottom:6px;'>"
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
