"""
Retrieves an article from Wikipedia (http://en.wikipedia.org).
"""
from pattern.web import Wikipedia

ENGINE = Wikipedia(language="en")


def main(search_query):
    """ Returns Twitter Search Results
    :param search_query: (str)
    """
    final = "Wikipedia Search Results:"
    article = ENGINE.search(search_query, cached=True, timeout=30)

    print article.title  # Article title (may differ from the search query).
    print ""
    print article.languages["tr"]   # Article in Turkish, can be retrieved with Wikipedia(language="tr").
    print article.links[:10]        # List of linked Wikipedia articles.
    print article.external[:5]      # List of external URL's.
    print ""

    for s in article.sections:
        final = final + "\n\n" + s.title.upper() + "\n" + s.content

    return final


if __name__ == '__main__':
    main("")
