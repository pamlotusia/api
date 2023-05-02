import mysql.connector
from flask import Flask, request

app = Flask(__name__)


con = mysql.connector.connect(
    host='localhost', database='aula_teste', user='root', password='pamela22')


@app.route('/funcionarios/buscar', methods=['GET'])
def buscar():
    cursor = con.cursor()
    cursor.execute('SELECT * FROM tb_aluno')
    resultado = cursor.fetchall()

    print(resultado)
    return resultado


@app.route('/funcionario/registrar', methods=['POST'])
def registrar():
    cursor = con.cursor()
    sql = "INSERT INTO tb_aluno (nome, sobrenome,turma) VALUES (%s, %s, %s)"
    valores = ("Joao Antonio", "Lima", "ADS")
    cursor.execute(sql, valores)
    con.commit()
    cursor.execute('SELECT * FROM tb_aluno') # para testar se o Post funcionou
    resultado = cursor.fetchall()
    return resultado


@app.route('/funcionario/deletar', methods=['DELETE'])
def deletar():
    cursor = con.cursor()
    sql = "DELETE FROM tb_aluno WHERE nome = 'Joao Antonio'"
    cursor.execute(sql)
    con.commit()
    cursor.execute('SELECT * FROM tb_aluno') # para testar se o Delete funcionou
    resultado = cursor.fetchall()
    return resultado


if __name__ == '__main__':
    app.run(debug=True)
