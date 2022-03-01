from flask import Blueprint, request, jsonify

api = Blueprint('api', 'api', url_prefix='/api')

@api.route("/pins", methods=["GET"])
def api_pins():
    from helpers import search_tag
    keyword = request.args.get("keyword")

    pins = search_tag(keyword)
    pins_json = [pin.to_json() for pin in pins]
    return jsonify(pins_json)