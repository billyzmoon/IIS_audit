from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Стартовая страница
@app.route('/')
def index():
    return render_template('index.html')

# Роут для GET-запросов
@app.route('/get', methods=['GET'])
def get_route():
    params = request.args
    return jsonify({param: value for param, value in params.items()})

# Роут для POST-запросов
@app.route('/post', methods=['POST'])
def post_route():
    params = request.form
    return jsonify({param: value for param, value in params.items()})

# Роут для HEAD-запросов
@app.route('/head', methods=['HEAD'])
def head_route():
    return '', 200

# Роут для OPTIONS-запросов
@app.route('/options', methods=['OPTIONS'])
def options_route():
    return '', 200

if __name__ == '__main__':
    app.run(debug=True)
