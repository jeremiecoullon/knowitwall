$(window.vent).on('showViewerCompleted', function() {
    // Force show current annotation if highlight clicked on.
    var toggledOnce = false;
    $('.annotator-hl').click(function () {
        if (toggledOnce) {
            return;
        }
        $('.annotator-viewer').toggleClass('annotator-viewer_show');
        toggledOnce = true;
    });

    // Find and replace text URLs into hyperlinks.
    var text = $('.annotator-annotation div').text();
    var regex = /(https?:\/\/([-\w\.]+)+(:\d+)?(\/([-\w\/_\.]*(\?\S+)?)?)?)/ig
    var replaced_text = text.replace(regex, "<a href='$1' target='_blank'>$1</a>");
    $('.annotator-annotation div').html(replaced_text);
});
