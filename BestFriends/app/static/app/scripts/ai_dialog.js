var max_message_index = -1

window.onload = function () {
	var sendButton = document.getElementById("talksubmit");
    var input_message = document.getElementById("input_words");
    var dialog = document.getElementById("chatting_dialog");
    var header = document.getElementById("head");

	///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

	// Define the actions to send a message
	input_message.addEventListener('keydown', function (e) {
		if (e.keyCode == 13) {
			send_message();
		}
	});

	sendButton.onclick = function () { send_message(); }
	///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
	// receive history messages
	var history_messages = new XMLHttpRequest();


	// when the response with history messages is received, display them on the dialog
	history_messages.onreadystatechange = function () {
		if (history_messages.readyState == 4) {
			console.log(history_messages.readyState + "historayra message ready");
			s = String(this.responseText);
			var response = JSON.parse(s);
            var messages = response.new_messages;

            console.log(message);
			console.log("loading history messages");

            var time = get_send_message_time();

			for (var i = 0; i < messages.length; i++) {
				var message = messages[i];
				console.log(message);

				if (max_message_index < message.message_index) {
					max_message_index = message.message_index;
				}
                
                message_text = message.message

                // the id of the sender who sent this message
                sender_name = message.sender_name

                //datetime of this message
                datetime = message.datetime

                var style = "";

                // decide the style by whether the message is from user
                if (message.is_from_user == false) {
                    style = "robot";
                }
                else {
                    style = "user";
                }
                dialog.innerHTML = dialog.innerHTML + ('<div class="' + style + '"><div class="message-time">' + datetime + '</div><span>' + message_text + '</span></div>' + '<div class="' + style + '"> <div class="show_name">'+" Sent by " + sender_name + '</div></div>');
                
                /*
                if (message.is_from_user == false) {
                    dialog.innerHTML = dialog.innerHTML + ('<div class="robot"><div class="message-time">'+ time[0] + "-" + time[1] + "-" + time[2] + "<br />" + time[3] + ":" + time[4] + ":" + time[5] +  '</div><span>' + message.message + '</span></div>' + '<div class="robot">' + " Sent by " + message.sender_name + '</div>');
                }
				else {
                    dialog.innerHTML = dialog.innerHTML + ('<div class="user"><div class="message-time">'+ time[0] + "-" + time[1] + "-" + time[2] + "<br />" + time[3] + ":" + time[4] + ":" + time[5] +  '</div><span>' + message.message + '</span></div>' + '<div class="user">' + " Sent by " + message.sender_name + '</div>');
				}
                header.innerHTML = time[0] + "-" + time[1] + "-" + time[2] + "<br />" + time[3] + ":" + time[4] + ":" + time[5];
                */
			}
			dialog.scrollTop = dialog.scrollHeight;
		}
	}

	// send a request asking for history messages
	history_messages.open("POST", "/api", true);
	json = JSON.stringify({
		"user_id": user_id, "message_index": max_message_index, 'type': 'message update'
	});
	history_messages.send(json);

    function send_message() {
        
		console.log(sendButton.readyState + " send button ready ");
		var str = "";
		if (input_message.value == "") {
			alert("Error! The message cannot be blank.");
			return;
		}
        else {

            var now_time = get_send_message_time();
			input_text = input_message.value;

            str = '<div class="user"><div class="message-time">' + now_time[0] + "-" + now_time[1] + "-" + now_time[2] + "<br />" + now_time[3] + ":" + now_time[4] + ":" + now_time[5] + '</div><span>' + input_text + '</span></div>';

			dialog.innerHTML = dialog.innerHTML + str;
            str = '<div class="user"><div class="show_name">' + " Sent by " + firstname + '</div></div>';
			dialog.innerHTML = dialog.innerHTML + str;

            input_message.value = "";
            

			dialog.scrollTop = dialog.scrollHeight;
		}


		var xhr = new XMLHttpRequest();
		xhr.open("POST", "/api", true);
		var json = JSON.stringify({
			'user_id': user_id, 'message': input_text, 'type': 'send message'
		});
		xhr.send(json);

		////////////////////////////////////////



		/////////////////////////////////////////////////////////////////




		sleep(4000);

		// and receive a response
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
                var get_time = get_send_message_time();

				for (var i = 0; i < messages.length; i++) {
					var message = messages[i];

					if (max_message_index < message.message_index) {
						max_message_index = message.message_index;
					}
                    
					message_text = message.message

					// the id of the sender who sent this message
					sender_name = message.sender_name

					//datetime of this message
					datetime = message.datetime

					var style = "";

					// decide the style by whether the message is from user
					if (!message.is_from_user) {

						style = "robot";
                        dialog.innerHTML = dialog.innerHTML + ('<div class="' + style + '"><div class="message-time">' + datetime + '</div><span>' + message_text + '</span></div>' + '<div class="' + style + '"><div class="show_name"> ' + " Sent by " + sender_name + '</div></div>');

					}
                    /*
					if (message.is_from_user == false) {
                        var get_time = get_send_message_time();
                        dialog.innerHTML = dialog.innerHTML + ('<div class="robot"><div class="message-time">'+ get_time[0] + "-" + get_time[1] + "-" + get_time[2] + "<br />" + get_time[3] + ":" + get_time[4] + ":" + get_time[5] +   '</div><span>' + message.message + '</span></div>' + '<div class="robot">' + " Sent by " + message.sender_name + '</div>');
                        header.innerHTML = get_time[0] + "-" + get_time[1] + "-" + get_time[2] + "<br />" + get_time[3] + ":" + get_time[4] + ":" + get_time[5];
                    }
                    */

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

    function get_send_message_time() {
        var now = new Date();
        var year = now.getFullYear();       
        var month = now.getMonth() + 1;     
        var day = now.getDate();            
        var h = now.getHours();
        var m = now.getMinutes();
        var s = now.getSeconds();
        var time = new Array(6);
        month = checkTime(month);
        day = checkTime(day);
        m = checkTime(m);
        s = checkTime(s);
        t = setTimeout('startTime()', 500);
        time[0] = String(year);
        time[1] = String(month);
        time[2] = String(day);
        time[3] = String(h);
        time[4] = String(m);
        time[5] = String(s);
        return time;
    }

    function checkTime(i) {
        if (i < 10) { i = "0" + i; }
        return i;
    }
}
	//////
