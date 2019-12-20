from bob import speak


def test_say_nothing_to_bob():
    phrase = ""

    assert speak(phrase) == "Whatever."


def test_say_statement_to_bob():
    phrase = "It's a lovely day outside."

    assert speak(phrase) == "Fine. Be that way!"


def test_ask_bob_question():
    phrase = "Are you going to dinner tonight?"

    assert speak(phrase) == "Sure"


def test_yell_statement_at_bob():
    phrase = "THE HOUSE IS A MESS!"

    assert speak(phrase) == "Whoa, chill out!"


def test_yell_question_at_bob():
    phrase = "WHY ARE YOU ALWAYS LATE?"

    assert speak(phrase) == "Calm down, I know what I'm doing"
