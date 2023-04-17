from flask import Flask
import json

app = Flask(__name__)

musicas = [
    {'id': 1, 'musica': 'Queimar', 'artista': 'OVEOUS', 'album': 'QUEMANDO'},
    {'id': 2, 'musica': 'Sonne', 'artista': 'Rammstein', 'album': 'Mutter'},
    {'id': 3, 'musica': 'A Pearl', 'artista': 'Mitski', 'album': ' Be the Cowboy'},
    {'id': 4, 'musica': 'Shut up My Moms Calling',
        'artista': 'Hotel Ugly', 'album': 'Shut up My Moms Calling'}
]

musicJSON = json.dumps(musicas)


@app.route('/musicas', methods=['GET'])
def musicas():
    return musicJSON, 202


if __name__ == '__main__':
    app.run(port=5000, debug=True, host='localhost')
