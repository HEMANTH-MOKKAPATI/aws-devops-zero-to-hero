from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, hemanth!, hemanth  How are You'

if __name__ == '__main__':
    app.run()

