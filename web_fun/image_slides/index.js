var pics = document.querySelectorAll(".slides__img");
function ScrollRight() {
	for(var i = 0; i < pics.length; ++i) {
		console.log(pics[i].width + pics[i].style.paddingLeft);
	}
}