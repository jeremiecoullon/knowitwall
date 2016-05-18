$(window.vent).on('showViewerCompleted', function() {
    // To parse the annotation, we've tried 3 different things so far.

    // 1. parses message as html
    var text = $('.annotator-annotation div').text();

    var knowit_title = "<img src='/static/Images/know-it.png' class='knowit_img'>"
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
