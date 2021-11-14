// Login button
function ChangeLoginValue() {
	if(this.value === "Login") {
		this.value = "Logout";
	}
	else {
		this.value = "Login"
	}
}
var login_button = document.querySelector(".header__login-btn");
login_button.onclick = ChangeLoginValue;

// Add definition button
function RemoveItem() {
	this.remove();
}
var add_def_btn = document.querySelector(".add-definition-card__btn");
add_def_btn.onclick = RemoveItem;


// Like buttons
var like_buttons = document.querySelectorAll(".dictionary-entry__like-btn");
for(var i in like_buttons) {
	like_buttons[i].onclick = function() {
		var num_likes = parseInt(this.value);
		num_likes += 1;
		this.value = num_likes + " likes";
	}
}