
window.onload = function () {
	var TalkSub = document.getElementById("talksub");
	var TalkWords = document.getElementById("talkwords");
	var Words = document.getElementById("words");
	TalkSub.onclick = function () {
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
				$('#words').html(Words.innerHTML + '<div class="atalk"><span>' + ret["answer_dict_name"] + '</span></div>');
			})
		}
		Words.innerHTML = Words.innerHTML + str;
		TalkWords.value = "";

	}
}