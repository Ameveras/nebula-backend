from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/api/get_message')
def get_message():
    id = request.args.get('id')
    name = request.args.get('name')
    return jsonify({"messages from " + id: ["Hello there " + name]})


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
