from flask import Flask, render_template, request

from spreadsheet import spreadsheet

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    info = ''
    if request.method == 'POST':
        req = request.form
        values = []
        num = 'e'
        add = []
        for item in req:
            if item[-1] == num:
                add.append(req[item])
            else:
                values.append(add)
                add = [req[item]]
                num = item[-1]
        values.append(add)
        spreadsheet(values)

    return render_template('index.html', info=info)


if __name__ == '__main__':
    app.run(debug=True, port=8000)
