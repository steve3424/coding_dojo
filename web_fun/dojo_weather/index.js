// Forecast cards that were already created
var active_forecasts = {};

var days_of_week = [
	"Sunday",
	"Monday",
	"Tuesday",
	"Wednesday",
	"Thursday",
	"Friday",
	"Saturday"
];

var img_paths = [
	"img/some_clouds.png",
	"img/some_rain.png",
	"img/some_sun.png",
];

var todays_date = new Date();
var day_index = todays_date.getDay();

var forecast_cards = document.querySelectorAll(".forecast-card");
function FillOutForecastCards() {
	var current_city = document.querySelector("#current-city");
	var cards = active_forecasts[current_city.innerHTML];
	if(cards) {
		for(var i = 0; i < forecast_cards.length; ++i) {
			var forecast_card = forecast_cards[i];
			forecast_card.innerHTML = cards[i];
		}

		if(document.querySelector("#temp-units-selector").value.includes("F")) {
			var highs = document.querySelectorAll(".forecast-card__high");
			var lows = document.querySelectorAll(".forecast-card__low");
			for(var i = 0; i < highs.length; ++i) {
				var forecast_card__high = highs[i];
				var forecast_card__low = lows[i];
				forecast_card__high.innerHTML = CtoF(forecast_card__high) + "&deg";
				forecast_card__low.innerHTML = CtoF(forecast_card__low) + "&deg";
			}
		}
	}
	else {
		active_forecasts[current_city.innerHTML] = [];
		cards = active_forecasts[current_city.innerHTML];

		for(var i = 0; i < forecast_cards.length; ++i) {
			var forecast_card = forecast_cards[i];
			// Set day
			var forecast_card__day = forecast_card.querySelector(".forecast-card__day");
			if(i === 0) {
				forecast_card__day.innerHTML = "Today";
			}
			else if(i === 1) {
				forecast_card__day.innerHTML = "Tomorrow";
			}
			else {
				var new_day_index = (day_index + i) % days_of_week.length;
				forecast_card__day.innerHTML = days_of_week[new_day_index];
			}
			
			// Set img
			var zero_one_two = Math.floor(Math.random() * 3);
			var img_path = img_paths[zero_one_two];
			var forecast_card__pic = forecast_card.querySelector(".forecast-card__pic");
			forecast_card__pic.src = img_path;
			
			// Set description
			var description = img_path.split("/")[1].split(".")[0].split("_").join(" ");
			var forecast_card__description = forecast_card.querySelector(".forecast-card__description");
			forecast_card__description.innerHTML = description;
			
			// Set temps
			// Hardcoded in celsius, convert to fahrenheit if necessary
			var forecast_card__high = forecast_card.querySelector(".forecast-card__high");
			var forecast_card__low = forecast_card.querySelector(".forecast-card__low");
			if(description.includes("sun")) {
				forecast_card__high.innerHTML = "28&deg";
				forecast_card__low.innerHTML = "16&deg";
			}
			else if(description.includes("rain")) {
				forecast_card__high.innerHTML = "16&deg";
				forecast_card__low.innerHTML = "5&deg";
			}
			else {
				forecast_card__high.innerHTML = "20&deg";
				forecast_card__low.innerHTML = "9&deg";
			}
			
			if(document.querySelector("#temp-units-selector").value.includes("F")) {
				forecast_card__high.innerHTML = CtoF(forecast_card__high) + "&deg";
				forecast_card__low.innerHTML = CtoF(forecast_card__low) + "&deg";
			}
	
			cards[i] = forecast_card.innerHTML;
		}
	}
}

FillOutForecastCards();

var forecast_card_days = document.querySelectorAll(".forecast-card__day");
for(var i = 0; i < forecast_card_days.length; ++i) {
}

// Cookie-accept action
var cookie_accept_btn = document.querySelector(".cookie-alert__accept-btn");
cookie_accept_btn.onclick = function() {
	this.parentElement.remove();
}

// City navigation
var current_city = document.querySelector("#current-city");
var cities = document.querySelectorAll(".header__city");
cities.forEach(element => {
	element.onclick = function() {
		if(this.innerHTML != current_city.innerHTML) {
			current_city.innerHTML = this.innerHTML;
			FillOutForecastCards();
		}
	}
});

// Temp conversion
var unit_selector = document.querySelector("#temp-units-selector");
unit_selector.onchange = function() {
	if(this.value.includes("F")) {
		for(var i = 0; i < forecast_cards.length; ++i) {
			var forecast_card__high = forecast_cards[i].querySelector(".forecast-card__high");
			var forecast_card__low = forecast_cards[i].querySelector(".forecast-card__low");
			forecast_card__high.innerHTML = CtoF(forecast_card__high) + "&deg";
			forecast_card__low.innerHTML = CtoF(forecast_card__low) + "&deg";
		}
	}
	else {
		for(var i = 0; i < forecast_cards.length; ++i) {
			var forecast_card__high = forecast_cards[i].querySelector(".forecast-card__high");
			var forecast_card__low = forecast_cards[i].querySelector(".forecast-card__low");
			forecast_card__high.innerHTML = FtoC(forecast_card__high) + "&deg";
			forecast_card__low.innerHTML = FtoC(forecast_card__low) + "&deg";
		}
	}
}

function FtoC(temp_el) {
	var temp = parseInt(temp_el.innerHTML);
	temp -= 32;
	temp *= 5 / 9;
	return Math.round(temp);
}

function CtoF(temp_el) {
	var temp = parseInt(temp_el.innerHTML);
	temp *= 9 / 5;
	temp += 32;
	return Math.round(temp);
}