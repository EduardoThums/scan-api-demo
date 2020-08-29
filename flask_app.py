from typing import Any
from uuid import uuid4

from flask import Flask, jsonify

app = Flask(__name__)


class Database:

    _TABLES = {
        'fighters': []
    }

    def save(self, new_object: Any, table_name: str) -> Any:
        new_object['id'] = str(uuid4())

        self._TABLES[table_name].append(new_object)

        return new_object

    def get(self, object_id: str, table_name: str) -> Any:
        try:
            found_object = next(filter(
                lambda item: item['id'] == object_id,
                self._TABLES[table_name]
            ))

            return found_object
        except Exception:
            return None


database = Database()


@app.route('/fighters', methods=['POST'])
def create_fighter():
    new_fighter = {
        'name': 'Akuma'
    }

    database.save(new_fighter, 'fighters')

    return jsonify(new_fighter)


@app.route('/fighters/<string:fighter_id>', methods=['GET'])
def get_fighter(fighter_id: str):
    fighter = database.get(fighter_id, 'fighters')

    return jsonify(fighter)


if __name__ == '__main__':
    app.run(debug=True)
