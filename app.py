import time
import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
	#seconds = 0
	#while seconds < 5:
	#	time.sleep(1)
	#	print(seconds)
	#	seconds +=1
	return render_template('timer.html')