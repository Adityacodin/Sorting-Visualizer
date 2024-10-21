from flask import Flask,request,url_for,render_template,jsonify
from sorting import SortingModule
from random import randint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
sort = SortingModule()

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/bubble')
def bubble_algo():
    sort.steps.clear()
    return jsonify(sort.bubble_sort([1,5,56,3,42,923,4]))

@app.route('/selection')
def selection_algo():
    sort.steps.clear()
    return jsonify(sort.selection_sort([1,5,56,3,42,923,4]))

@app.route('/insertion')
def insertion_algo():
    sort.steps.clear()
    return jsonify(sort.insertion_sort([1,5,56,3,42,923,4]))

@app.route('/merge')
def merge_algo():
    sort.steps.clear()
    return jsonify(sort.merge_sort([1,5,56,3,42,923,4],0,6))

@app.route('/quick')
def quick_algo():
    pass

@app.route('/getdt', methods=['POST'])
def process():
    try:
        data = request.json
        print("Received data:", data)
        if not data:
            return jsonify({'error': 'No data received'}), 400
        size = int(data.get('size'))
        algo = data.get('algo')
        array = [randint(0, 100) for _ in range(size)]
        return jsonify({
            'message': 'Data received successfully',
            # 'size': size,
            # 'algorithm': algo
            'array' : array
        }), 200
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': 'Internal Server Error', 'details': str(e)}), 500


if __name__ == "__main__":
    app.run()