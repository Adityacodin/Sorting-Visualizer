from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def start():
    return render_template('index.html')


def selection_sort(arr):
    for i in range(len(arr)-1):
        min_num = arr[i]
        min_index = i
        for j in range(len(arr)):
            if arr[j] < min_num:
                min_num = arr[j]
                min_index = j
        
        temp = arr[min_index]
        arr[min_index] = arr[i]
        arr[i] = temp
    return arr


if __name__ == "__main__":
    app.run()