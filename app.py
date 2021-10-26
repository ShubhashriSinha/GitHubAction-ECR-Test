from flask import Flask, render_template
import subprocess

app=Flask("myapp")

@app.route("/mail")
def myemail():
	return render_template("e.html")

@app.route("/search")
def mysearch():
	data=subprocess.getoutput("date")
	return(data)