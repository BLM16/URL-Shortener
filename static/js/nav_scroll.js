$(document).ready(function () {
    if ($(window).scrollTop() > 56)
        $(".navbar").addClass("bg-dark");
    else
        $(".navbar").removeClass("bg-dark");

    $(window).scroll(() => {
        if ($(".navbar-collapse").hasClass("show"))
            return
        
        if ($(window).scrollTop() > 56)
            $(".navbar").addClass("bg-dark");
        else
            $(".navbar").removeClass("bg-dark");
    });
    
    $(".navbar-toggler").click(() => {
        if (!$(".navbar-collapse").hasClass("show"))
            $(".navbar").addClass("bg-dark");
        else
            $(".navbar").removeClass("bg-dark");
    });
});
