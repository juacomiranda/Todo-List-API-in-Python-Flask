from flask import Flask, jsonify, request,json
app = Flask(__name__)

todo = [{   "label": "My first task", "done": False }]
decoded_object = json.loads(todo)


@app.route('/todos', methods=['GET'])
def hello_world ():
    json_text = jsonify(todo)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    return jsonify(todo)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todo.remove("My first task")
    return jsonify(todo)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)