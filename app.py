from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    info = ''
    if request.method == 'POST':
        req = request.form
        print(req)
        for item in req:
            print(item)
    return render_template('index.html', info=info)


if __name__ == '__main__':
    app.run(debug=True)
