def speak(phrase):
    if phrase.isupper():
        return (
            "Calm down, I know what I'm doing"
            if phrase.endswith("?")
            else "Whoa, chill out!"
        )

    elif phrase.endswith("?"):
        return "Sure"

    elif phrase.endswith("."):
        return "Fine. Be that way!"
    return "Whatever."
