import os
from dotenv import load_dotenv
import pickle
from flask import Flask, render_template, request, redirect, url_for, session
from player import Player
from enemy import Enemy
from quiz import Quiz

app = Flask(__name__)
load_dotenv()
app.secret_key = os.getenv("SECRET_KEY")

quiz = Quiz()

# Creăm lista de inamici
enemies = [Enemy("Goblin", 10, 1), Enemy("Orc", 30, 2), Enemy("Zombie", 50, 3), Enemy("Chicken", 70, 4), Enemy("Dragon", 100, 5)]


@app.route("/", methods=["GET", "POST"])
def index():
    msg = ""
    if "player" not in session:
        player = Player("Jucator", 100)
        session["player"] = pickle.dumps(player)
        session["enemy_index"] = 0
        enemy = enemies[0]   # creezi enemy local
        session["enemy"] = pickle.dumps(enemy)
    else:
        player = pickle.loads(session["player"])
        enemy = pickle.loads(session["enemy"])

    if "current_question" not in session:
        question_data = quiz.get_quiz_question()
        session["current_question"] = question_data
    else:
        question_data = session["current_question"]

    question, answers, correct_index = question_data


    if request.method == "POST":
        choice = int(request.form["choice"])
        if choice + 1 == correct_index:
            enemy.take_damage(10)
            msg = "Corect! Enemy pierde 10 HP."
        else:
            player.take_damage(10)
            msg = "Greșit! Tu pierzi 10 HP."

        session.pop("current_question", None)

        # Verificăm câștig / pierdere
        if enemy.health <= 0:
            session["enemy_index"] += 1
            if session["enemy_index"] < len(enemies):
                enemy = enemies[session["enemy_index"]]
                msg += f" Ai trecut la nivelul următor: {enemy.name}"
            else:
                msg += " Felicitări! Ai terminat toți inamicii."
                session.clear()
                return redirect(url_for("index"))

        elif player.health <= 0:
            msg += " Ai pierdut jocul..."
            session.clear()
            return redirect(url_for("index"))

        # Salvăm starea obiectelor
        session["player"] = pickle.dumps(player)
        session["enemy"] = pickle.dumps(enemy)

    return render_template("index.html",
                       question=question,
                       answers=list(enumerate(answers, start=0)),
                       msg=msg,
                       player_hp=player.health,
                       enemy_hp=enemy.health,
                       enemy_name=enemy.name)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
