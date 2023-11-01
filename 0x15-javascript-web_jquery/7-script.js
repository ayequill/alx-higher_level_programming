$.ajax({
  type: 'GET',
  url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
  success: (response) => $('div#character').text(response.name)
});
