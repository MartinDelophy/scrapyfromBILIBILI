from flask import Flask
from flask import render_template

from scrapy import res

app = Flask(__name__, static_url_path='')


@app.route('/')
def show():
	print ("success")
	return render_template('index.html')


@app.route('/api/v1/datasource', methods=['GET', 'POST'])
def datasource():

	return res

if __name__ == '__main__':
	
	app.run()