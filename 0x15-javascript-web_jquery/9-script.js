$.ajax({
    url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
    type: 'GET',
    success: (res) => $('DIV#hello').text(res.hello)

})
