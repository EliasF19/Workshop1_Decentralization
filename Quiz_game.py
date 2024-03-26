# quiz_game.py

def load_questions():
    return [
        {"question": "Quelle est la plus petite planète du système solaire ?", "answer": "Mercure"},
        {"question": "Qui a écrit 'Les Misérables' ?", "answer": "Victor Hugo"},
        {"question": "Quel est l'élément chimique ayant pour symbole 'Au' ?", "answer": "Or"},
        {"question": "Dans quel pays se trouve la ville de Timbuktu ?", "answer": "Mali"},
        {"question": "Quelle année a vu le premier pas de l'homme sur la Lune ?", "answer": "1969"},
        {"question": "Qui a peint 'La nuit étoilée' ?", "answer": "Vincent van Gogh"},
        {"question": "Quel est l'océan le plus profond du monde ?", "answer": "Pacifique"},
        {"question": "Quel est le nom du président français pendant la Seconde Guerre mondiale ?", "answer": "Charles de Gaulle"},
        {"question": "Quel est le livre le plus vendu au monde après la Bible ?", "answer": "Le Petit Prince"},
        {"question": "Qui a inventé le téléphone ?", "answer": "Alexander Graham Bell"}
    ]


def run_quiz(questions):
    score = 0
    for q in questions:
        user_answer = input(q["question"] + " ")
        if user_answer.lower() == q["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print(f"Your final score is: {score}/{len(questions)}")

def main():
    questions = load_questions()
    run_quiz(questions)

if __name__ == "__main__":
    main()
