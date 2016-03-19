from flask import Flask, request

app = Flask(__name__)

@app.route('/github_streak')
def github_streak():
    return request.data

if __name__ == "__main__":
    app.run()
