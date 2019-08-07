from flask import Flask, request, render_template, jsonify

app = Flask(__name__, static_url_path="")

@app.route("/")
def index():
    """Return the main page."""
    return app.send_static_file("index.html")


@app.route("/output", methods=["GET", "POST"])
def output():
    """Retun text from user input"""
    data = request.get_json(force=True)
    # every time the user_input identifier
    print(data)
    return jsonify({"user_output": data["user_input"]})

