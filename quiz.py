import random

class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "Care este capitala Franței?",
                "answers": ["Berlin", "Paris", "Roma"],
                "correct_index": 2
            },
            {
                "question": "Cât face 5 * 6?",
                "answers": ["11", "30", "56"],
                "correct_index": 2
            },
            {
                "question": "Ce limbaj folosim aici?",
                "answers": ["C++", "Python", "Java"],
                "correct_index": 2
            },
            {
                "question": "Care este cel mai mare ocean de pe Pământ?",
                "answers": ["Atlantic", "Pacific", "Indian"],
                "correct_index": 2
            },
            {
                "question": "Cine a pictat Mona Lisa?",
                "answers": ["Michelangelo", "Leonardo da Vinci", "Raphael"],
                "correct_index": 2
            },
            {
                "question": "Câte continente există?",
                "answers": ["5", "6", "7"],
                "correct_index": 3
            },
            {
                "question": "Care este elementul chimic cu simbolul 'O'?",
                "answers": ["Osmium", "Oxigen", "Oganesson"],
                "correct_index": 2
            },
            {
                "question": "Cine a scris 'Romeo și Julieta'?",
                "answers": ["Shakespeare", "Hemingway", "Dante"],
                "correct_index": 1
            },
            {
                "question": "Ce planetă este a patra de la Soare?",
                "answers": ["Marte", "Venus", "Jupiter"],
                "correct_index": 1
            },
            {
                "question": "Care este moneda Japoniei?",
                "answers": ["Yen", "Won", "Dollar"],
                "correct_index": 1
            }
        ]

    def get_quiz_question(self):
        q = random.choice(self.questions)
        return q["question"], q["answers"], q["correct_index"]
