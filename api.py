import paralleldots

paralleldots.set_api_key('FxrLIwX0pCmWAU3xr9ZttM0whrwX7MQB7HNmHAh8OhU')


def ner(text):
    ner = paralleldots.ner(text)
    return ner


def sentiment(text):
    sentiment = paralleldots.sentiment(text)
    return sentiment


def abuse(text):
    abuse = paralleldots.abuse(text)
    return abuse
