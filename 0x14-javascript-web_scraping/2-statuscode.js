#!/usr/bin/node
require('request').get(process.argv[2], (err, response) => {
	if (err){
		console.log(err);
	}else{
		console.log('code: ' + response.statuscode)}
});
