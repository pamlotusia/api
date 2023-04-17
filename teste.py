from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/v1/aula', methods=["GET"])
def consultar():
    return 'primeira chamada de api!'



@app.route('/v1/aula', methods=["POST"])
def cadastrar():
    # input_json = request.get_json(force=True)
    # camada de banco de dados
    jsonToReturn = {
        'Cadastro': 'Você não tem autorização'}
    return jsonToReturn


if __name__ == '__main__':
    app.run(debug=True, port=5001, host="localhost")
