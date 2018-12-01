var max_message_index = -1

window.onload = function () {
	var sendButton = document.getElementById("talksub");
	var input_message = document.getElementById("talkwords");
	var dialog = document.getElementById("words");

	var historary_messages = new XMLHttpRequest();
	////////
	input_message.addEventListener('keydown', function (e) {
		if (e.keyCode == 13) {
			send_message();
		}
	});

	sendButton.onclick = function () { send_message(); }
	/////////

	historary_messages.onreadystatechange = function () {
		if (historary_messages.readyState == 4) {
			console.log(historary_messages.readyState + "historayra message ready");
			s = String(this.responseText);
			var response = JSON.parse(s);
			var messages = response.new_messages

			console.log(message)
			console.log("loading history messages");

			for (var i = 0; i < messages.length; i++) {
				var message = messages[i];
				console.log(message);

				if (max_message_index < message.message_index) {
					max_message_index = message.message_index;
				}

				if (message.is_from_user == false) {
					dialog.innerHTML = dialog.innerHTML + ('<div class="atalk"><span>' + message.message + '</span></div>' + '<div class="atalk">' + "Sent by " + message.sender_name + '</div>');
				}
				else {
					dialog.innerHTML = dialog.innerHTML + ('<div class="btalk"><span>' + message.message + '</span></div>' + '<div class="btalk">' + "Sent by " + message.sender_name + '</div>');

				}

			}
			dialog.scrollTop = dialog.scrollHeight;
		}
	}

	historary_messages.open("POST", "/api", true);



	json = JSON.stringify({
		"user_id": user_id, "message_index": max_message_index, 'type': 'message update'
	});

	historary_messages.send(json);







	function send_message() {

		console.log(sendButton.readyState + "send button ready");
		var str = "";
		if (input_message.value == "") {
			alert("error!");
			return;
		}
		else {
			input_text = input_message.value;

			str = '<div class="btalk"><span>' + input_text + '</span></div>';

			dialog.innerHTML = dialog.innerHTML + str;
			str = '<div class="btalk">' + "Sent by " + firstname + '</div>';
			dialog.innerHTML = dialog.innerHTML + str;

			input_message.value = "";
			dialog.scrollTop = dialog.scrollHeight;
		}

		///////send message



		var xhr = new XMLHttpRequest();
		xhr.open("POST", "/api", true);
		var json = JSON.stringify({
			'user_id': user_id, 'message': input_text, 'type': 'send message'
		});
		xhr.send(json);

		////////////////////////////////////////



		/////////////////////////////////////////////////////////////////




		sleep(4000);
		var update_message = new XMLHttpRequest();

		update_message.onreadystatechange = function () {
			if (update_message.readyState == 4) {
				s = String(this.responseText);
				var response = JSON.parse(s);
				try {
					var messages = response.new_messages
				} catch (error) {
					;
				} finally {
					;
				}
				console.log(messages);

				for (var i = 0; i < messages.length; i++) {
					var message = messages[i];

					if (max_message_index < message.message_index) {
						max_message_index = message.message_index;
					}

					if (message.is_from_user == false) {
						dialog.innerHTML = dialog.innerHTML + ('<div class="atalk"><span>' + message.message + '</span></div>' + '<div class="atalk">' + "Sent by " + message.sender_name + '</div>');
					}


				}
				dialog.scrollTop = dialog.scrollHeight;
			}

		}


		update_message.open("POST", "/api", true);



		json = JSON.stringify({
			"user_id": user_id, "message_index": max_message_index, 'type': 'message update'
		});

		update_message.send(json);

	}

	function sleep(delay) {
		var start = new Date().getTime();
		while (new Date().getTime() < start + delay);
	}

}
	//////
