$('document').ready(function () {
  $('#btn_translate').click(function () {
    const lang1 = $('#language_code').val();
    $.get(`https://hellosalut.stefanbohacek.dev/?lang=${lang1}`, function (obj) {
      $('#hello').text(obj.hello);
    });
  });
});
