
from flask import Flask, render_template, redirect, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'magodegelo123'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/calcular', methods=['POST'])
def calcular():
    altura = request.form.get('altura')
    laterais = request.form.get('laterais')

    return redirect('/')

    return render_template()

 



 if __name__ in '__main__':
    app.run(debug=True)



