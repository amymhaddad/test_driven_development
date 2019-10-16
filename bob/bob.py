
# phrase = "WHY ARE YOU ALWAYS LATE?"

def speak(phrase):
    if phrase.isupper():
        return "Calm down, I know what I'm doing" if phrase.endswith("?") else 'Whoa, chill out!'

    elif phrase.endswith("?"):
        return 'Sure'

