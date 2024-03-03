from flask import Blueprint, render_template, request
from .rock_paper_scissors import check
from .utils.helpers import response
routes = Blueprint("routes", __name__)

@routes.get("/")
def home_page():
  return render_template("index.html")


@routes.post("/check")
def check_result():
  try:
    data = request.get_json()
    if not data.get("choice"): raise Exception("Please select a choice")
    return check(data.get('choice'))
  except Exception as err:
    return response(str(err), None, False)
