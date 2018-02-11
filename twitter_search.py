"""
Retrieves tweets containing given keywords from Twitter.
"""
from pattern.web import Twitter, hashtags
from pattern.db  import Datasheet, pprint, pd

ENGINE = Twitter(language="en")


def main(search_query):
    """ Returns Twitter Search Results
    :param search_query: (str)
    """
    final = "Twitter Search Results:"
    for i in range(2):
        print(i)
        for tweet in ENGINE.search(search_query, start=None, count=25,
                                   cached=False):

            final = final + "\n\n" + tweet.text + "\n" + \
                    tweet.author + "\n" + tweet.date + "\n" + \
                    str(hashtags(tweet.text))  # Keywords in tweets start with a "#".
    return final


if __name__ == '__main__':
    main("")
