#!/usr/bin/node
const request = require('request');
const url = 'http://swapi.co/api/films/' + process.argv[2];
request(url, (error, reponse, body) => {
	console.log(error || JSON.parse(body).title);
});
