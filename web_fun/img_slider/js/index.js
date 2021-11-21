var img = 0;
var pic = document.querySelector("#pic");
var slider = document.querySelector("#width-adjust");
var btn = document.querySelector("#btn");

pic.width = slider.value;
slider.oninput = function() {
	pic.width = this.value;
}
btn.onclick = function() {
	if(img === 0) {
		pic.src = "../img/heisencat.png";
		img = 1
	}
	else {
		pic.src = "../img/daftpunktocat-thomas.gif";
		img = 0;
	}
	pic.width = slider.value;
}