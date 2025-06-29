from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze/<text>', methods=['GET'])
def analyze(text):
    sentiment = "positive" if "good" in text else "negative"
    return jsonify({"sentiment": sentiment})

if __name__ == '__main__':
    app.run(port=5000)
