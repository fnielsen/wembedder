"""Views for app."""

import re

from flask import (
    Blueprint, current_app, jsonify, redirect, render_template, request,  
    Response, url_for)
from werkzeug.routing import BaseConverter


class RegexConverter(BaseConverter):
    """Converter for regular expression routes.

    References
    ----------
    https://stackoverflow.com/questions/5870188

    """

    def __init__(self, url_map, *items):
        """Setup regular expression matcher."""
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]


def add_app_url_map_converter(self, func, name=None):
    """Register a custom URL map converters, available application wide.

    References
    ----------
    https://coderwall.com/p/gnafxa/adding-custom-url-map-converters-to-flask-blueprint-objects

    """
    def register_converter(state):
        state.app.url_map.converters[name or func.__name__] = func

    self.record_once(register_converter)



Blueprint.add_app_url_map_converter = add_app_url_map_converter
main = Blueprint('app', __name__)
main.add_app_url_map_converter(RegexConverter, 'regex')

# Wikidata item identifier matcher
q_pattern = '<regex("Q[1-9]\d*"):q>'
Q_PATTERN = re.compile(r'Q[1-9]\d*')


@main.route("/")
def index():
    """Return rendered index page.

    Returns
    -------
    html : str
        Rederende HTML for index page.

    """
    return render_template('index.html')


@main.route('/most-similar/' + q_pattern)
@main.route('/most-similar/')
def show_most_similiar(q=None):
    language = 'da'
    return render_template('most-similar.html', q=q, language=language)


@main.route('/api/most-similar/' + q_pattern)
def api_most_similar(q):
    """Return JSON for most similar.

    Parameters
    ----------
    q : str
        Wikidata item identifier.

    Returns
    -------
    response : str.
        String with JSON.

    """
    try:
        most_similar = current_app.model.most_similar(q)
    except KeyError:
        message = {
            'status': 404,
            'message': 'Not found: ' + q
        }
        response = jsonify(message)
        response.status_code = 404
        return response
    except:
        # Ups!
        message = {
            'status': 500,
            'message': 'Unhandled error'
        }
        response = jsonify(message)
        response.status_code = 500
        return response
    
    data = {
        'most_similar': [
            { 'item': item, 'similarity': similarity }
            for item, similarity in most_similar
        ],
        'model_metadata': current_app.model.metadata
    }
    response = jsonify(data)
    return response
