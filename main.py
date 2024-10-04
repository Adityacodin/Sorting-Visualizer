from flask import Flask,render_template,jsonify
from sorting import SortingModule


app = Flask(__name__)
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

def quick_algo():
    pass

if __name__ == "__main__":
    app.run()