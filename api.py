''' Created 2019-05-19 by NGnius '''

from flask import request, abort, Blueprint, jsonify
from lib.recipe_scrapers.recipe_scrapers import scrape_me as scrape_recipe

# api_bp should not be overwritten
try:
    api_bp
except NameError:
    api_bp = Blueprint('api', __name__, url_prefix='/api')

class APIController():
    ''' Controller class for binding routes to flask app '''
    def __init__(self, app):
        app.register_blueprint(api_bp)
        self.app = app

''' Routes '''
@api_bp.route('/', methods=['GET', 'POST'])
def root():
    website = get_param('url', request)
    if website is None:
        abort(400)
    website_json = to_jsonable(scrape_recipe(website))
    return jsonify(website_json)

''' Helper functions '''
def get_param(param, request, silent=False):
    if request.method == 'GET':
        return request.args.get(param)
    else:
        try:
            return request.get_json(force=True, silent=silent)[param]
        except KeyError:
            return None

JSON_FORM = {
            'host': lambda recipe : recipe.host(),
            'title': lambda recipe : recipe.title(),
            'total_time': lambda recipe : recipe.total_time(),
            'ingredients': lambda recipe : recipe.ingredients(),
            'instructions': lambda recipe : recipe.instructions(),
            'ratings':lambda recipe : recipe.ratings(),
            'reviews':lambda recipe : recipe.reviews(),
            'links':lambda recipe : recipe.links()
            }
def to_jsonable(recipe):
    res = {}
    for key in JSON_FORM:
        try:
            value = JSON_FORM[key](recipe)
        except NotImplementedError:
            value = None
        res[key] = value
    return res
