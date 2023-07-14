import wikipedia

# nlp
from textblob import TextBlob


def wiki(name="apple", length=1):
    """this is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki


# for search
def search_wiki(name):
    """Search wikipedia for names"""

    result = wikipedia.search(name)
    return result


# nlp phrases
def phrase(name):
    """Returns phrases from wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
