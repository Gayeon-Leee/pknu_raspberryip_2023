from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_World():
	return "Hello world"

@app.route('/name')
def namefunc():
	return "Yoo Kihyun"

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="9000") 
	# 0.0.0.0 은 외부 접속 허가하는 것
