$(document).ready(function () {
    $('.view-solution-trigger').click(function () {
        window.location.href = '/solution-detail.html';
    });
    $('.navbar-icon-container .trigger').click(function () {
        let entity = $.trim($(this).text());
        if (entity == 'home')
            window.location.href = '/home.html';
        $(this).parent().siblings().removeClass('active');
        $(this).parent().siblings().find('.menu-panel').removeClass('d-flex').addClass('d-none');
        $(this).parent().siblings().find('.floating-menu').removeClass('active');
        $(this).parent().find('.menu-panel').toggleClass('d-none d-flex');
        $(this).parent().addClass('active');
        $(this).parent().find('.floating-menu').toggleClass('active');
    });
    $('.icon-round').click(function ($e) {
        $e.stopPropagation();
    });
    // $('.carousel').on('slide.bs.carousel', function (e) {
    //     // Disallow carousel movement in case of less elements
    //     var $e = $(e.relatedTarget);
    //     var idx = $e.index();
    //     var itemsPerSlide = 3;
    //     var totalItems = $(this).find('.carousel-item').length;
    //     if (totalItems <= itemsPerSlide)
    //         return false;
    // });
});