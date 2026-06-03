from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! Welcome to CI/CD Lab!'

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'running',
        'message': 'CI/CD pipeline is working!'
    })

@app.route('/api/greet/<name>')
def greet(name):
    return jsonify({
        'message': f'Hello, {name}!',
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
