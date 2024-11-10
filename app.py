from flask import Flask, render_template, request
from web import setup_browser, play_youtube_video
import threading

app = Flask(__name__)

video_thread = None;
global stop_video

#Front end rendering
@app.route('/home',methods=["GET"])
def home():
	return render_template('index.html')

	
#backend handling

@app.route('/play', methods=["GET"])
def play_video():
	driver = setup_browser()
	link= request.args.get("link")
	video_thread = threading.Thread(target=play_youtube_video,args=(link,driver))
	play_youtube_video(link,driver)
	return"link submitted"
	
@app.route('/stop', methods=["GET"])	
def stop_playback():
	global stop_video
	stop_video=True
	return {"code":204}
if __name__ == '__main__':
	app.run( debug= True,host ='0.0.0.0',port=5000)
	print("server Live")
