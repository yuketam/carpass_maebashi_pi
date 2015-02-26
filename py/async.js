var fs = require('fs');

setTimeout(function() {
	console.log('node async process running', process.argv);
	process.exit(1);
}, 2500);