$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (obj) {
  $('#character').text(obj.name);
});
