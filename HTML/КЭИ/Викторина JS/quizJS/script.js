var Mass = ["1 вопрос","2 вопрос","3 вопрос"];

var Answers = ["1","2","3"];

var Result = document.getElementById("result");

function testStart () {

	for(var i=0;i<Mass.length;i++) {
		var answer = prompt(Mass[i]);
		Result.innerHTML += "<div class='item item" + i + "'>" + answer + "</div>";

		if (answer == Answers[i]) {
			Result.innerHTML += "<div class='answer answer" + "-true" + "'>" + "верно" + "</div>" + "</br>";
		} else {
			Result.innerHTML += "<div class='answer answer" + "-false" + "'>" + "неверно" + "</div>" + "</br>";
		}

	}

}