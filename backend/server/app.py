from flask import Flask, jsonify, request
from flask_cors import CORS

from main import Arcade2048

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

game = Arcade2048()

# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@app.route('/api/solo/is_ready', methods=['GET'])
def is_ready():
    return jsonify({'message':'ready'})

@app.route('/api/solo/init', methods=['GET'])
def solo_init():
    global game
    game = Arcade2048()
    return jsonify({'message': 'Initialisation de la partie solo'})

@app.route('/api/solo/get_grid', methods=['GET'])
def get_grid():
    global game
    return game.get_grid()

@app.route('/api/solo/get_score', methods=['GET'])
def get_score():
    global game
    score = game.get_score()
    return jsonify({'score': score})

@app.route('/api/solo/move', methods=['POST'])
def solo_move():
    global game

    data = request.get_json()
    direction = data.get('direction')
    match direction:
        case 'up':
            game.move_up()
            return jsonify({'has_moved': True, 'game_ended':not game.get_more_moves(), 'has_won':game.won()})
        case 'down':
            game.move_down()
            return jsonify({'has_moved': True, 'game_ended':not game.get_more_moves(), 'has_won':game.won()})

        case 'left':
            game.move_left()
            return jsonify({'has_moved': True, 'game_ended':not game.get_more_moves(), 'has_won':game.won()})

        case 'right':
            game.move_right()
            return jsonify({'has_moved': True, 'game_ended':not game.get_more_moves(), 'has_won':game.won()})

        # Incorrect direction
        case _:
            return jsonify({'has_moved': False}), 400

@app.route('/api/solo/save_score', methods=['POST'])
def solo_save_score_update_leaderboard():
    global game

    data = request.get_json()
    pseudo,score = data.get('pseudo'), data.get('score')
    is_leaderboard_updated = game.update_leaderboard(pseudo, score)

    if is_leaderboard_updated:
        return jsonify({'success': True}), 200
    return jsonify({'success': False}), 400

@app.route('/api/solo/get_leaderboard', methods=['GET'])
def get_leaderboard():
    global game
    return game.get_leaderboard()

@app.route('/api/solo/game_reset', methods=['GET'])
def solo_game_reset():
    """
    Open a popup to end the game or just pause the game
    :return:
    """
    global game
    state = game.reset()
    return jsonify({'is_reset': state})

if __name__ == '__main__':
    app.run()