var table_rows = document.querySelectorAll(".table__row")
for(var i = 0; i < table_rows.length; ++i) {
	table_rows[i].onmouseover = function() {
		this.style.fontWeight = "bold";
	}
	table_rows[i].onmouseleave = function() {
		this.style.fontWeight = "normal";
	}
}