from flask import Flask, render_template, request
import webbrowser

app = Flask(__name__)



#Front end rendering
@app.route('/home',methods=["GET"])
def home():
	return render_template('index.html')
	
	
	
#backend handling

@app.route('/play', methods=["GET"])
def play_video():
	link= request.args.get("link")
	webbrowser.open(link)
	
	
	
	return"link submitted"
	
	
if __name__ == '__main__':
	app.run( debug= True,host ='0.0.0.0',port=5000)
	print("server Live")
