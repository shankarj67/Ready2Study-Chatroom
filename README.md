# Ready2study Chat

This repository contains a Chat Client that demonstrate the features of the
Python Socket.IO server in combination with Flask.

## How to Run

First create a virtual environment and import the requirements.



To start the server, run:

```
(venv) $ export FLASK_APP=socketio_examples.py
(venv) $ flask run
```

If you are using Windows Environment:

```
(venv) $ set FLASK_APP=socketio_examples.py
(venv) $ flask run
```

If you want to use this on your friend's laptop or PC

Note: You must be in same network in order to chat.

```
(venv) $ flask run --host=0.0.0.0
```

Finally, open _http://localhost:5000_ on your web browser to access the
application.

On your friend's laptop open _http://your_ip_address:5000_


