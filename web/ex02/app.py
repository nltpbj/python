from flask import Flask, render_template
from routes import bbs

app = Flask(__name__, template_folder="templates")
app.register_blueprint(bbs.bp)

@app.route("/")
def index():
    return "hello"

if __name__=='__main__':
    app.run(port=5000, debug=True)