const url_re = /^(?:http)s?:\/\/(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})(?::\d+)?(?:\/?|[/?]\S+)$/gi;

document.getElementById("txtURL").addEventListener('keyup', function() {
    let txt = $(this).val();

    if (!url_re.test(txt))
        $(this).addClass('is-invalid');
    else
        $(this).removeClass('is-invalid');
});
