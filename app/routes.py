from flask import Blueprint, request, jsonify
from app.services import fetch_stop_and_search_data
from app.utils import validate_date

bp = Blueprint("routes", __name__)

@bp.route("/stop-and-search/outcome", methods=["GET"])
def stop_and_search_outcome():
    force = request.args.get("force")
    date = request.args.get("date")

    if not force or not date:
        return jsonify({"error": "Both 'force' and 'date' parameters are required."}), 400

    if not validate_date(date):
        return jsonify({"error": "Invalid date format. Use YYYY-MM."}), 400

    try:
        result = fetch_stop_and_search_data(force, date)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": "An error occurred.", "details": str(e)}), 500