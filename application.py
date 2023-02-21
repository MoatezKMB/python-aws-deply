from flask import Flask
application= Flask(__name__)
@application.route('/')

def hello_mouatez():
    return 'hello KARABAGHLI Mouatez Bellah'
