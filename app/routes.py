from flask import Blueprint, request, jsonify
from app.services import fetch_stop_and_search_data
from app.utils import validate_date

bp = Blueprint("routes", __name__)

@bp.route("/stop-and-search/outcome", methods=["GET"])
def stop_and_search_outcome():
    """
        Handle the stop and search outcome request.
        
        This function retrieves the 'force' and 'date' parameters from the request,
        validates them, and fetches the stop and search data for the specified force
        and date. If the parameters are missing or invalid, it returns an appropriate
        error message.
        
        Returns:
            Response: A JSON response containing the stop and search data or an error message.
            
        Query Parameters:
            force (str): The police force to retrieve data for.
            date (str): The date in YYYY-MM format to retrieve data for.
            
        Responses:
            200: A JSON object containing the stop and search data.
            400: A JSON object with an error message if 'force' or 'date' is missing or invalid.
            500: A JSON object with an error message if an internal error occurs.
    """
    
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