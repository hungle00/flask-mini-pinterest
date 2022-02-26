from flask import Blueprint, request, jsonify

api = Blueprint('api', 'api', url_prefix='/api')

@api.route("/pins", methods=["GET"])
def api_pins():
    from helpers import search_tag
    keyword = request.args.get("keyword")

    results = search_tag(keyword)
    return jsonify(results)