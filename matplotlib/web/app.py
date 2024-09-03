from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html', title='시각화')

if __name__=='__main__':
    app.run(port=500, debug=True)