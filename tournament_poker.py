import logging

from flask import Flask, render_template
from flask_ask import Ask, question, session, statement

from poker.decision import make_tournament_decision
from poker.utilities import is_correct_input


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


@ask.launch
def new_tournament():
    welcome_message = render_template('welcome')
    return question(welcome_message)


@ask.intent("AMAZON.YesIntent")
def next_hand():
    next_hand_msg = render_template('next_hand')
    return question(next_hand_msg)


@ask.intent("AnswerIntent",
            convert={'stack_size': int},
            mapping={'first_card': 'firstCard',
                     'second_card': 'secondCard',
                     'stack_size': 'stackSize',
                     'position': 'position'})
def answer(first_card, second_card, stack_size, position):
    correct_input = is_correct_input(
        first_card, second_card, stack_size, position)

    if correct_input:
        push_decision = make_tournament_decision(
            first_card, second_card, stack_size, position)
        if push_decision:
            msg = render_template('push')
        else:
            msg = render_template('dont_push')
    else:
        msg = render_template('wrong_input')

    return statement(msg)


if __name__ == '__main__':
    app.run(host='localhost', port=80, debug=True)
