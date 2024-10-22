from flask import Flask,request,url_for,render_template,jsonify
from sorting import SortingModule
from random import randint
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
sort = SortingModule()
array = None

@app.route('/')
def start():
    return render_template('index.html')


def select_algo(algo):
    if algo == 'bubble':
        bubble_algo()
    elif algo == 'selection':
        selection_algo()
    elif algo == 'insertion':
        insertion_algo()
    elif algo == 'merge':
        merge_algo()
    elif algo == 'quick':
        quick_algo()

def bubble_algo():
    sort.steps.clear()
    sort.bubble_sort(array)

def selection_algo():
    sort.steps.clear()
    sort.selection_sort(array)

def insertion_algo():
    sort.steps.clear()
    sort.insertion_sort(array)

def merge_algo():
    sort.steps.clear()
    sort.merge_sort(array,0,len(array)-1)

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
        global array
        array = [randint(0, 100) for _ in range(size)]
        select_algo(algo)
        return jsonify({
            'message': 'Data received successfully',
            # 'size': size,
            # 'algorithm': algo
            'array' : array,
            'sort_steps' : sort.steps
        }), 200
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': 'Internal Server Error', 'details': str(e)}), 500


if __name__ == "__main__":
    app.run()