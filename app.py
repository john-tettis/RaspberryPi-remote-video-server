from flask import Flask, render_template, request
from web import setup_browser, play_youtube_video


app = Flask(__name__)


#Front end rendering
@app.route('/home',methods=["GET"])
def home():
	return render_template('index.html')

	
#backend handling

@app.route('/play', methods=["GET"])
def play_video():
	driver = setup_browser()
	link= request.args.get("link")
	play_youtube_video(link,driver)
	return"link submitted"
	
	
if __name__ == '__main__':
	app.run( debug= True,host ='0.0.0.0',port=5000)
	print("server Live")
