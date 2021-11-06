function AddLikeBtnHandlers() {
	var like_btns = document.querySelectorAll(".feed-card__like-btn");
	for(var i = 0; i < like_btns.length; ++i) {
		like_btns[i].addEventListener("click", function() {
			var parent_el = this.parentElement;
			var num_likes = parent_el.querySelector(".feed-card__num-likes");
			var number = parseInt(num_likes.innerHTML.replace(/\D/g, ''));
			number++;
			num_likes.innerHTML = number + " like(s)";
		})
	}
}

AddLikeBtnHandlers();