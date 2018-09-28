import os
from flask import Flask, render_template
from flask_socketio import SocketIO


app = Flask(__name__)
app.config['FILEDIR'] = 'static/_files/'
app.config['CHAT_URL'] = os.environ.get('CHAT_URL')
socketio = SocketIO(app)

from chat import bp as chat_bp


app.register_blueprint(chat_bp, url_prefix='/chat')



@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
