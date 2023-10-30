import redis

from flask import Flask, jsonify, request


app = Flask(__name__)

r = redis.Redis(host='redis', port=6379, decode_responses=True)
redis_key = 'ram_load'


@app.route('/ram_overload/', methods=['GET'])
def get_last_ram_overload():
    if not r.get(redis_key):
        return jsonify({'message': 'ram wasnt overload'}), 200
    else:
        return jsonify({redis_key: r.get(redis_key)}), 200


@app.route('/add_overload_value/', methods=['POST', 'PUT'])
def post_ram_overload():
    query = request.form[redis_key]
    if not query:
        return jsonify({'error': 'no query params in request'})

    if float(query) >= 90.0:
        r.set(redis_key, float(query))
        return jsonify({redis_key: float(query)}), 201
    else:
        return jsonify({'error': 'ram load value must be more 90'}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
