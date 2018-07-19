if(navigator.webkitGetUserMedia!=null) { 
	var options = { 
        video:true, 
        audio:false 
    };
	
	navigator.webkitGetUserMedia(options, 
        function(stream) { 
            var video = document.querySelector('video'); 
            video.src = window.webkitURL.createObjectURL(stream); 
        }, 
        function(e) { 
			alert("You need to allow webcam access for this page");
            console.log("There was a problem with webkitGetUserMedia"); 
        } 
    );  
		
}

