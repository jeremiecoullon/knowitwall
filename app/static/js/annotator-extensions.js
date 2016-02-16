$(window.vent).on('showViewerCompleted', function() {
    var toggledOnce = false;
    $('.annotator-hl').click(function () {
        if (toggledOnce) {
            return;
        }
        $('.annotator-viewer').toggleClass('annotator-viewer_show');
        toggledOnce = true;
    });
});