from flask import Flask  # importando biblioteca

app = Flask(__name__)


@app.route('/api1')  # request
def home():
    return 'texto de retorno'


if __name__ == '__main__':  # iniciar servidor
    app.run(debug=True)
