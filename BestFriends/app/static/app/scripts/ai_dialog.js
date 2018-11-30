
window.onload = function () {
	var TalkSub = document.getElementById("talksub");
	var TalkWords = document.getElementById("talkwords");
	var Words = document.getElementById("words");


	TalkSub.onclick = function () {
		var xhr = new XMLHttpRequest();
		xhr.onreadystatechange = function () {
			console.log(this.responseText);
		}

		xhr.open("POST", "/api", true);
		var json = JSON.stringify({ 'hello': 'value1' });
		xhr.send(json);







		var str = "";
		if (TalkWords.value == "") {
			alert("error!");
			return;
		}

		else {
			str = '<div class="btalk"><span>' + TalkWords.value + '</span></div>';
			//$.get("/js_ai", { 'Twords': TalkWords.value }, function (ret) {
			//    $('#result').html(ret);
			//})
			$.getJSON("/js_ai", { 'Twords': TalkWords.value }, function (ret) {
				//alert(ret["answer_dict_name"]);
				$('#words').html(Words.innerHTML + '<div class="atalk"><span>' + ret["answer_dict_name"] + '</span></div>' + '<div class="atalk">' + "Sent by bot" + '</div>');
			})
		}
		Words.innerHTML = Words.innerHTML + str;
		str = '<div class="btalk">' + "Sent by " + firstname + '</div>';
		Words.innerHTML = Words.innerHTML + str;

		TalkWords.value = "";

	}
}