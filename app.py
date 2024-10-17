from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    n = int(request.args.get('n', 0))
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])
    return jsonify(fibonacci=fib[n])

@app.route('/')
def hello_world():
    return "Hello World from Raspberry Pi"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

