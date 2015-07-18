from flask import Flask, render_template
from tumblelog import app 

@app.route('/')
def index():
	return "<h1>hello</h1>"
