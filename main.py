from flask import Flask, request, redirect, render_template
#need to add a database
app = Flask(__name__, static_folder='static')

@app.route('/')
def index():
    return render_template('webpage.html')


@app.route('/log/')
def log():
    return render_template('login2.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file:
        file.save('uploads/' + file.filename)
        return 'File uploaded successfully!'
    else:
        return 'No file selected.'

@app.route('/dashb/')
def dashb():
    return render_template('dashboard.html')

@app.route('/settings/')
def settings():
    return render_template('settings.html')

@app.route('/loading/')
def loading():
    return render_template('loading.html')

@app.route('/prediction/')
def prediction():
    return render_template('prediction.html')

@app.route('/reviews/')
def reviews():
    return render_template('reviews.html')
@app.route('/upl/')
def upl():
    return render_template('upload.html')

@app.route('/predict/')
def predict():
    return render_template('model.html')
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username == 'admin' and password == 'password':
        return redirect('/dashb')
    else:
        return redirect('/log/')

@app.route('/dashboard')
def dashboard():
    return render_template('drag drop.html')

@app.route('/about/')
def about():
    return render_template('About us.html')

if __name__ == '__main__':
    app.run(debug=True)
