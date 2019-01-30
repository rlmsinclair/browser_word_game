from flask import Flask, request, render_template
import CurrentLetters
import InputLetter

app = Flask(__name__, static_url_path='', static_folder='static')


current_letters = CurrentLetters.CurrentLetters()
input_letter = InputLetter.InputLetter()

@app.route('/')
def root():
    return app.send_static_file('index.html')


@app.route('/wordgame/')
def wordgame():
    return app.send_static_file('wordgame/index.html')


@app.route('/wordgame/game/')
def start_game():
    return current_letters.get_letters() + '<br><br><br><br>' + render_template('my-form.html')


@app.route('/wordgame/game/', methods=['POST'])
def enter_letter():
    text = request.form['text']
    processed_text = text.upper()[0]
    input_letter.set_input_letter(processed_text)
    return current_letters.get_letters() + '<br><br>' + processed_text + '<br><br>' + render_template('front_or_back.html')


@app.route('/wordgame/game/front/')
def add_letter_to_front():
    current_letters.add_letter_to_front(input_letter.get_input_letter())
    return current_letters.get_letters() + '<br><br><br><br>' + render_template('continue.html')


@app.route('/wordgame/game/back/')
def add_letter_to_back():
    current_letters.add_letter_to_back(input_letter.get_input_letter())
    return current_letters.get_letters() + '<br><br><br><br>' + render_template('continue.html')
