import wikipedia


def wiki(name="apple", length=1):
    """this is a wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, length)
    return my_wiki
