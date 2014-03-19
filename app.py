from flask import Flask, jsonify ,request, render_template
from random import randint
from sendgrid import Mail, SendGridClient
app = Flask(__name__)
app.debug = True
 
tweets = [{"text": "jinja2", "id": 1}]
 
@app.route('/', methods=['GET'])
def render_page():
	return render_template('index.html', tweets=tweets)
 
@app.route('/tweets', methods=['POST','GET'])
def create_tweet():
	if request.method == 'POST':	
		newtweet = {'id': randint(0, 256), 'text': request_form['tweet']}
		tweets.append(newtweet)
		return jsonify(newtweet)#or return tweets
		#return jsonify(tweets.append({"text":request.form['tweet'],"id":randint(0,256)}))
	else:
		#obtener todos los tweets
		return jsonify({"tweets":tweets})
 
 
			#para poder enviarle el id
@app.route('/tweets/<int:id>', methods=['GET', 'DELETE'])
def single_tweet(id):
	if request.method == 'GET':
		#serve single tweet
		for tweet in tweets:
			if tweet.id == id:
				return jsonify(tweet)
		#si no encuentra nada devuelve un hash vacio
		#siempre hay q devolver algo aunque sea vacio
		return jsonify({})
	else:
		#delete single tweet
		for tweet in tweets:
			removed = tweet
			tweets.remove(tweet)
			return jsonify(removed)
			#if tweet.id == id:
				#tweets.remove
			#	return jsonify(tweet)
 
		return jsonify({'error': 'not found'})

#here we add the email functionality, for later
 
if __name__ == "__main__": 
	app.run()
