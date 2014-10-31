var fonts = {
	1:"Changa One",
	2: "Playball",
	3:"Comfortaa",
	4:"Indie Flower",
	5:"Permanent Marker"
};

var num;

var setNum = function(){
	num = Math.floor((Math.random()*Object.keys(fonts).length)+1);
};

var getLink = function(){
	return "http://fonts.googleapis.com/css?family=" + fonts[num].split(' ').join('+');
};

var getCSS = function() {
    return fonts[num];
};
