$('document').ready(function () {
  $.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (obj) {
    $('#hello').text(obj.hello);
  });
});
