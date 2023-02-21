'''from flask import Flask
application= Flask(__name__)
@application.route('/')

def hello_mouatez():
    return 'hello KARABAGHLI Mouatez Bellah'

hello_mouatez()'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)