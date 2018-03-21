#!/usr/bin/env python
# Ignore Invalid constant name
# pylint: disable=C0103
# Ignore no-self-use
# pylint: disable=R0201
"""
Used for API_server between actual code and UI. This server needs to be
running while requesting something via UI.
"""

from flask import Flask
from flask_restful import reqparse, Api, Resource

import google_search
import twitter_search
import wikipedia_search

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('category')
parser.add_argument('text_form')


@app.after_request
def after_request(response):
    """
    Controls flask api requests.
    :param response: response feature of flask
    :return: response
    """
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers',
                         'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response


class MyFlask(Resource):
    """
    /niog
    """
    def post(self):
        """
        Creates Index Report
        """
        args = parser.parse_args()
        category = args['category']
        text_form = args['text_form']
        print "Running for {}!".format(category)
        
        if category.lower() == "google search":
            return google_search.main(text_form)
        elif category.lower() == "twitter":
            return twitter_search.main(text_form)
        elif category.lower() == "wikipedia":
            return wikipedia_search.main(text_form)


api.add_resource(MyFlask, '/niog')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True, port=5000)
