from flask import Flask, render_template
from flask_talisman import Talisman

app = Flask(__name__)
Talisman(app)

@app.route('/')
def home():
    return render_template('form.html')

if __name__ == '__main__':
    app.run(ssl_context=('cert.pem', 'key.pem'))

