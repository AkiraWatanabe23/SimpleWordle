'''テスト'''
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    '''テスト'''
    if request.method == 'GET':
        return render_template('index.html')
    else:
        form_input = request.form['input']
        return render_template('index.html', form_input=form_input)

if __name__ == '__main__':
    app.run(debug=True)
    