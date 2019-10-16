
from bob import speak 

def test_ask_bob_question():
    phrase = "Are you going to dinner tonight?"

    assert speak(phrase) == 'Sure'


def test_yell_statement_at_bob():
    phrase = "YOU CAME HOME AFTER MIDNIGHT!"

    assert speak(phrase) == "Whoa, chill out!"


def test_yell_question_at_bob():
    phrase = "WHY ARE YOU ALWAYS LATE?"

    assert speak(phrase) == "Calm down, I know what I'm doing"