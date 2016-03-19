from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>GitHub card web server</h1>'

@app.route('/github_streak', methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def github_streak():
    return request.data

if __name__ == "__main__":
    app.run(host='0.0.0.0')
