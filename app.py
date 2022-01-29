import json

from flask import Flask, jsonify, request

import producer

app = Flask(__name__)


@app.route('/health')
def health():
    return jsonify({'response': 'Hello World!'})


@app.route('/api/orders/computers', methods=['POST'])
def computers():
        request_body = request.get_json(force=True)
        print (request_body)
        return jsonify(producer.orders(request_body))
    

if __name__ == '__main__':
    app.run()