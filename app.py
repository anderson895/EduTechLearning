from flask import Flask, render_template, jsonify

app = Flask(__name__)
app.secret_key = 'AWLJDIAWLWAD'



@app.route('/')
def landing():
    return render_template('index.html')



# if __name__ == '__main__':
#     app.run(port=5001, debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)