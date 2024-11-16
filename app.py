from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to something secure

# Load words from the data file
def load_words():
    with open("/home/rizwan/Desktop/Django/Character-Gusssing-Game-with-python/static/data/scrabble.json", "r") as file:
        words = [line.strip() for line in file.readlines() if len(line.strip()) > 4 and len(line.strip()) <= 12]
    return words

words_list = load_words()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start", methods=["POST"])
def start_game():
    # Choose a random word for the game
    session["word"] = random.choice(words_list)
    session["attempts"] = 0
    session["guesses"] = []
    return redirect(url_for("game"))

@app.route("/game")
def game():
    if "word" not in session:
        return redirect(url_for("index"))
    masked_word = "".join([char if idx in session.get("correct_indices", []) else "-" for idx, char in enumerate(session["word"])])
    return render_template("game.html", masked_word=masked_word, attempts=session["attempts"], guesses=session["guesses"])

@app.route("/guess", methods=["POST"])
def guess():
    if "word" not in session:
        return redirect(url_for("index"))

    guessed_word = request.form.get("guess", "").strip().lower()
    session["attempts"] += 1
    session["guesses"].append(guessed_word)

    if guessed_word == session["word"]:
        return redirect(url_for("result", result="win"))

    if session["attempts"] >= 10:
        return redirect(url_for("result", result="lose"))

    correct_indices = [idx for idx, char in enumerate(session["word"]) if idx < len(guessed_word) and guessed_word[idx] == char]
    session["correct_indices"] = correct_indices
    return redirect(url_for("game"))

@app.route("/result/<result>")
def result(result):
    word = session.get("word", "N/A")
    return render_template("result.html", result=result, word=word)

if __name__ == "__main__":
    app.run(debug=True)
