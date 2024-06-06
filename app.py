from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

responses = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    edad = request.form.get('edad')
    birthdate = request.form.get('birthdate')
    location = request.form.get('location')

    response = {
        'name': name,
        'edad': edad,
        'birthdate': birthdate,
        'location': location
    }
    responses.append(response)
    return redirect(url_for('response_list'))

@app.route('/responses')
def response_list():
    return render_template('responses.html', responses=responses)

if __name__ == '__main__':
    app.run(debug=True)
