// Set up login button behavior
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


// Set up add definition btn behavior
function RemoveItem() {
	this.remove();
}

var add_def_btn = document.querySelector(".add-definition-card__btn");
add_def_btn.onclick = RemoveItem;