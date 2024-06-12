$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (obj) {
  for (let i = 0; i < obj.results.length; i++) {
    $('#list_movies').append(`<LI>${obj.results[i].title}</LI>`);
  }
});
