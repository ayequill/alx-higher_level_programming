$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
  success: (response) => response.results.forEach(film => { $('ul#list_movies').append(`<li>${film.title}</li>`); })
});
