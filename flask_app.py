from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/fighters', methods=['POST'])
def create_fighter():
    new_fighter = {
        'name': 'Akuma'
    }

    return jsonify(new_fighter)


if __name__ == '__main__':
    app.run(debug=True)
