from flask import Flask, jsonify  # importando bibliotecas

app = Flask(__name__)


@app.route('/api2')  # request
def main():
    return jsonify(professor='Alexandre')


if __name__ == '__main__':  # iniciando servidor
    app.run(port=5000, debug=True)
