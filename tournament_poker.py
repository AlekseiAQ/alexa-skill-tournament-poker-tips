import logging
from random import randint

from flask import Flask, render_template
from flask_ask import Ask, question, session, statement

app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


if __name__ == '__main__':
    app.run(debug=True)
