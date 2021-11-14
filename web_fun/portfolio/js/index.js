var bod = document.body;
var groovy_text_elements = document.getElementsByClassName("groovy_text");

var request_id = null;

var page_is_groovy = false;
function SubmitAction() {
	if(page_is_groovy) {
		if(window.confirm("Wanna stop groovin'?")) {
			page_is_groovy = false;

			bod.style.backgroundColor = "rgb(255, 255, 255)";
			for(var i = 0; i < groovy_text_elements.length; ++i) {
				groovy_text_elements[i].style.color = "rgb(0, 0, 0)";
			}
			window.cancelAnimationFrame(request_id);
		}
	}
	else {
		if(window.confirm("Wanna get groovy?")) {
			page_is_groovy = true;

			StartGroove();
			request_id = requestAnimationFrame(Groove);
		}
	}

	return false;
}

// Returns [0, max) exclusive since
// Math.random() will never be 1.0
function GetRandomInt(max) {
	return Math.floor(Math.random() * max);
}

var bg_colors = [];
var bg_deltas = [1, -2, 3];
var txt_colors = [];
var txt_deltas = [-1, 2, -3];
function StartGroove() {
	// Set up background color.
	for(var i = 0; i < 3; ++i) {
		bg_colors[i] = GetRandomInt(256);
		txt_colors[i] = GetRandomInt(256);
	}

	// Set background color.
	var bg_color_string = "rgb(" + bg_colors[0] + "," +
	                    bg_colors[1] + "," +
						bg_colors[2] + ")";
	bod.style.backgroundColor = bg_color_string;

	// Set text color.
	var txt_color_string = "rgb(" + txt_colors[0] + "," +
	                    txt_colors[1] + "," +
						txt_colors[2] + ")";
	for(var i = 0; i < groovy_text_elements.length; ++i) {
		groovy_text_elements[i].style.color = txt_color_string;
	}
}

function Groove(time_stamp) {
	for(var i = 0; i < 3; ++i) {
		// Bounds check bg_colors.
		if(bg_colors[i] <= 0) {
			if(bg_deltas[i] < 0) {
				bg_deltas[i] = bg_deltas[i] * -1;
			}
		}
		else if(bg_colors[i] >= 255) {
			if(bg_deltas[i] > 0) {
				bg_deltas[i] = bg_deltas[i] * -1;
			}
		}

		// Bounds check txt_colors.
		if(txt_colors[i] <= 0) {
			if(txt_deltas[i] < 0) {
				txt_deltas[i] = txt_deltas[i] * -1;
			}
		}
		else if(txt_colors[i] >= 255) {
			if(txt_deltas[i] > 0) {
				txt_deltas[i] = txt_deltas[i] * -1;
			}
		}

		// Update color vals
		bg_colors[i] += bg_deltas[i];
		txt_colors[i] += txt_deltas[i];
	}

	// Update element color attribs
	var bg_color_string = "rgb(" + bg_colors[0] + "," +
	                    bg_colors[1] + "," +
						bg_colors[2] + ")";
	bod.style.backgroundColor = bg_color_string;

	var txt_color_string = "rgb(" + txt_colors[0] + "," +
	                    txt_colors[1] + "," +
						txt_colors[2] + ")";
	for(var i = 0; i < groovy_text_elements.length; ++i) {
		groovy_text_elements[i].style.color = txt_color_string;
	}
	
	request_id = requestAnimationFrame(Groove);
}