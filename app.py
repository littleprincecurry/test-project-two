from flask import Flask, render_template, jsonify, request
from flask_pymongo import PyMongo
from os import environ
import json


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/news'

mongo = PyMongo(app)


@app.route('/')
def index():
    headlines = mongo.db.headlines.find({})
    data = []

    for headline in headlines:
        item = {
            '_id': str(headline['_id']),
            'Keyword': headline['Keyword'],
            'Source': headline['Source'],
            'Author': headline['Author'],
            'Title': headline['Title'],
            'URL': headline['URL'],
            'Text': headline['Text'],
            'Published': headline['Published'],
            'compound score': headline['compound score'],
            'negative score': headline['negative score'],
            'neutral score': headline['neutral score'],
            'Full Text Clean': headline['Full Text Clean']
        }
        data.append(item)

    return render_template('index.html', data=data)


@app.route('/news')
def news():
    headlines = mongo.db.headlines.find({})
    data = []

    for headline in headlines:
        item = {
            '_id': str(headline['_id']),
            'Keyword': headline['Keyword'],
            'Source': headline['Source'],
            'Author': headline['Author'],
            'Title': headline['Title'],
            'URL': headline['URL'],
            'Text': headline['Text'],
            'Published': headline['Published'],
            'compound score': headline['compound score'],
            'negative score': headline['negative score'],
            'neutral score': headline['neutral score'],
            'Full Text Clean': headline['Full Text Clean']
        }
        data.append(item)

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
