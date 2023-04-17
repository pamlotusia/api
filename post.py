from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/v1/aula/cadastrar', methods=["POST"])
def cadastrar():
    input_json = request.get_json(force=True)
    # camada de banco de dados
    jsonToReturn = {
        'nome': input_json['nome'], 'Cadastro': 'Para efetuar o cadastro passe o seu código'}
    return jsonify(jsonToReturn)


@app.route('/v1/aula/consultar', methods=["GET"])
def consultar():
    # return jsonify(list(range(5)))
    return 'primeira chamada de api!'


# http://localhost:5000/deletar/5
@app.route('/v1/aula/deletar/<int:number>/', methods=["DELETE"])
def deletar(number):
    return "Excluido " + str(number)
    # return "Excluido " + str(number), 401


@app.route('/v1/aula/atualizar', methods=["PUT"])
def atualizar():
    input_json = request.get_json(force=True)
    # banco de dados
    jsonToReturn = {'text': input_json['text'], 'text2': input_json['text2']}
    return jsonify(jsonToReturn)


if __name__ == '__main__':
    app.run()
