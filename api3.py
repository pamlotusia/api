from flask import Flask, request  # Importa a biblioteca

app = Flask(__name__)  # Inicializa a aplicação


@app.route('/api3')  # Nova rota
def main():
    resultado = 'Entre as notas na URL'

    primeira = request.args.get('primeira')
    segunda = request.args.get('segunda')

    if primeira and segunda:

        primeira = float(primeira)
        segunda = float(segunda)

        media = (primeira + segunda) / 2
        if media >= 7:
            resultado = 'Aprovado'
        elif media >= 4 and media < 7:
            resultado = 'Recuperação'
        else:
            resultado = 'Reprovado'

    return f'{resultado}: {media}'


if __name__ == '__main__':
    app.run(debug=True)  # Executa a aplicação
