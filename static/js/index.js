$(document).ready(function () {
    setup();
});

var menuSetup = function () {
    $('#home')
        .visibility({
            once: false,
            onBottomPassed: function () {
                $('.fixed.menu').transition('fade in');
            },
            onBottomPassedReverse: function () {
                $('.fixed.menu').transition('fade out');
            }
        })
    ;

    // create sidebar and attach to menu open
    $('.ui.sidebar')
        .sidebar('attach events', '.toc.item');
    $('.ui.dropdown').dropdown();
};


var setup = function () {
    menuSetup();
    $(".search.dropdown").dropdown({
        onChange: function (val) {
            console.log(val);
            $('html, body').animate({
                scrollTop: $('#' + val).offset().top
            }, 1000);
            //$.scrollTo($('#' + val), 1000);
        }
    });
};