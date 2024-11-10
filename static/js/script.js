
//grab our html elements
const form = document.getElementById('link-form')
const linkInput = document.getElementById('link-input')
const stopButton = document.getElementById('stop-button')
const submit =  document.getElementById('submit-button')
const loadingScreen = document.getElementById("loading-screen")
//toggle loading screen after form submission
function toggleLoadingScreen(isLoading){
	let on, off;
	if(isLoading){
		on = loadingScreen
		off = form;
	}
	else{
		off= loadingScreen;
		on = form;
	}
	off.style.display = "none"
	on.style.display ="block"
	
}
//send request to the play endpoint to start video playback
function send_youtube_url(link){
	fetch(`/play?link=${encodeURIComponent(link)}`)
	.then(response=>response.json())
	.then(data=>{
		console.log(data)
		}).catch(err=>console.error(err))
}
function stop_playback(){
	fetch(`/stop`)
	.then(response=>response.json())
	.then(data=>{
		console.log(data)
		}).catch(err=>console.error(err))
}
	


stopButton.addEventListener('click',(e)=>{
	e.preventDefault()
	stop_playback()
	toggleLoadingScreen(false)
	
	
	
})
form.addEventListener("submit",(e)=>{
	//prevent form from redirecting immediately
	e.preventDefault()
	toggleLoadingScreen(true)
	send_youtube_url(linkInput.value)
});

