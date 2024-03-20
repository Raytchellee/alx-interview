#!/usr/bin/node

const req = require('request');

req(
  'https://swapi-api.hbtn.io/api/films/' + process.argv[2],
  function (error, response, responseBody) {
    if (error) throw error;
    const characters = JSON.parse(responseBody).characters;
    fetchCharacters(characters, 0);
  }
);

const fetchCharacters = (characters, idx) => {
  if (idx === characters.length) return;
  req(characters[idx], function (error, response, responseBody) {
    if (error) throw error;
    console.log(JSON.parse(responseBody).name);
    fetchCharacters(characters, idx + 1);
  });
};
