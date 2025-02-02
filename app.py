from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.secret_key = 'AWLJDIAWLWAD'



@app.route('/')
def landing():
    return render_template('index.html')



@app.route('/lesson1')
def lesson1():
    return render_template('lesson1.html')


@app.route('/lesson2')
def lesson2():
    return render_template('lesson2.html')


@app.route('/lesson3')
def lesson3():
    return render_template('lesson3.html')


@app.route('/lesson4')
def lesson4():
    return render_template('lesson4.html')


@app.route('/lesson5')
def lesson5():
    return render_template('lesson5.html')


@app.route('/lesson6')
def lesson6():
    return render_template('lesson6.html')




# if __name__ == '__main__':
#     app.run(port=5001, debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)