var accept_buttons = document.getElementsByClassName("person__accept");
var reject_buttons = document.getElementsByClassName("person__reject");
var current_friends_list = document.getElementById("current-friends-list");

// Add click handler to all person__reject buttons
for(var i in reject_buttons) {
	reject_buttons[i].onclick = function () {
		// Decrease connection count
		var num_connections_element = document.getElementById("num-connections");
		var num_connections = parseInt(num_connections_element.innerHTML);
		num_connections -= 1;
		num_connections_element.innerHTML = num_connections;

		// Remove HTML element
		this.parentElement.parentElement.remove();

		// If connections is 0 display the message
		if(num_connections === 0) {
			var no_connections_msg_el = document.getElementById("no-connections-msg");
			no_connections_msg_el.style.display = "block";
		}
	}
}

// Add click handler to all person__accept buttons
for(var i in accept_buttons) {
	accept_buttons[i].onclick = function () {
		// Decrease connection count
		var num_connections_element = document.getElementById("num-connections");
		var num_connections = parseInt(num_connections_element.innerHTML);
		num_connections -= 1;
		num_connections_element.innerHTML = num_connections;

		// If connections is 0 display the message
		if(num_connections === 0) {
			var no_connections_msg_el = document.getElementById("no-connections-msg");
			no_connections_msg_el.style.display = "block";
		}

		// Increase friend count
		var num_friends_element = document.getElementById("num-friends");
		var num_friends = parseInt(num_friends_element.innerHTML);
		num_friends += 1;
		num_friends_element.innerHTML = num_friends;

		// Remove accept-reject buttons from person element
		// since this will be moving to current friends list
		var person_block = this.parentElement.parentElement;
		person_block.getElementsByClassName("person__accept-reject-wrapper")[0].remove();
		current_friends_list.appendChild(person_block);
	}
}

// Add sign out click handler
var sign_out_btn = document.getElementById("sign-out-btn");
sign_out_btn.onclick = function () {
	window.location.href = "../html/bye.html";
}