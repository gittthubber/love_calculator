from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def index():
    title = 'Love Calculator'
    return render_template('index.html', title=title)

@app.route('/score', methods=['POST'])
def score():
    title = 'Score'
    first_name = request.form.get('first_name')
    second_name = request.form.get('second_name')
    possibilities = ['Antonio', 'antonio', 'Simona', 'simona']
    
    if first_name and second_name:
        if first_name in possibilities and second_name in possibilities:
            perfect = random.randint(97, 110)
            return render_template('score.html', title=title, first_name=first_name, second_name=second_name, perfect=perfect)
        else:
            worst = random.randint(1, 5)
            return render_template('score.html', title=title, first_name=first_name, second_name=second_name, worst=worst)
    else:
        return render_template('score.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)
