$(function () {
    $('.nav-sidebar>li>a').click(function (event) {
        var that = $(this);
        if (that.children('a').attr('href') == '#') {
            event.preventDefault();
        }
        if (that.parent().hasClass('unfold')) {
            that.parent().removeClass('unfold');
        } else {
            that.parent().addClass('unfold').siblings().removeClass('unfold');
        }
        console.log('coming....');
    });

    $('.nav-sidebar a').mouseleave(function () {
        $(this).css('text-decoration', 'none');
    });
});