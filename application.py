from flask import Flask
application= Flask(__name__)
@application.route('/')

def hello_mouatez():
    return 'hello Mouatez Bellah'
if __name__ == '__main__':
    application.run()