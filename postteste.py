from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/teste/teste1', methods=["GET"])
def teste():
    return jsonify(list(range(5)))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
