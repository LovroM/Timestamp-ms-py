from flask import Flask, render_template, jsonify

app = Flask(__name__)




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/<ext_url>")
def url_input(ext_url):
    return jsonify(request = ext_url)
    


### Runs server
if __name__ == "__main__":
    app.debug = True
    app.run(host = "0.0.0.0", port = 8080)