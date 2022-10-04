//Hook up the tweet display

$(document).ready(function() {
						   
	$(".countdown").countdown({
				date: "9 dec 2022 18:00:00",
				format: "on"
			},
			
			function() {
				// callback function
			});

});	