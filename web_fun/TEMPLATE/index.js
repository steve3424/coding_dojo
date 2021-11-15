var delta = 1.0 / 30.0;
var header = document.getElementById("header");
header.style.opacity = "1.0";

function MainLoop(time_stamp) {
	var op = parseFloat(header.style.opacity);
	
	if(op >= 1.0) {
		delta *= -1.0;
	}

	if(op <= 0) {
		delta *= -1.0;
	}

	op += delta;

	header.style.opacity = op.toString();

	requestAnimationFrame(MainLoop);
}

requestAnimationFrame(MainLoop);
