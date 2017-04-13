"""
Generate markov text from text files and post to Twitter.
"""

from random import choice
import sys
import os           # Access our OS environment variables
import twitter      # Importing twitter module on lab machines

def open_and_read_file(file_path):
    """
    
    Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and 
    Turns the file's contents as one string of text.
    
    """

    # Read the file, return text as a string titled "contents"
    contents = open(file_path).read()

    # Return contents of your file as one long string
    return contents

def make_chains(text_string):
    """
    
    Takes input text as string; returns dictionary of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'juanita'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

    """

    # Split text string into a list of words
    words = text_string.split()

    # Create dictionary
    chains = {}

    # Iterate over the index numbers of the list
    for i in range(len(words)-2):
        
        # Create a tuple of two n-grams
        bigrams = (words[i], words[i+1])

        # Check for repeat of keys / bigrams
        if bigrams not in chains:

            # If the key doesn't exists, add key to chains
            chains[bigrams] = [words[i+2]]

       # If bigram is in the list, append value to the type list
        else:
            chains[bigrams].append(words[i+2])

    # Import pprint
    # Pprint.pprint(chains)
    return chains

def make_text(chains):
    """
    Returns text from chains.
    """

    words = []

    # Set random tuple to variable key
    key = choice(chains.keys())


    # First time through key in chains, unpack X - a tuple - to get  
    # key[0], key[1]  = key
    # print key0]
    # print key[2]
    # Append key[0], key[1] to words

    words.append(key[0])
    words.append(key[1])

    # While tuple is a key in chains, keep looping 
    while key in chains:

        # Randomly choose a value from chains
        word = choice(chains[key])

        # Append word to words
        words.append(word)

        key = (key[1], word)

    # return " ".join(words)

    # define variable of returned " ".join(words) as markov-tweet
    markov_tweet = " ".join(words)

    return markov_tweet


def tweet(markov_tweet):

    # Set max. 140 characters 
    markov_tweet = markov_tweet[:140]

    # Post random Markov chain text to Twitter

    # Using Python os.environ to get environmental variables
    # Reminder: Run `source secrets.sh` before running 
    # this file to set required environmental variables.

    api = twitter.Api(
        consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'])

    # Print info about credentials to make sure they're correct
    print api.VerifyCredentials()

    # Send a tweet
    status = api.PostUpdate(markov_tweet)
    print status.text

    # If you updated secrets.sh, you can go to your Twitter 
    # timeline to see it.

# Assign greens-eggs.txt to variable
input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Print chains       <-- do this to test a portion of this exercise

# Produce random text
random_text = make_text(chains)

tweet(random_text)

# Mission Accomplished! We're TWITS! Code reviewed by Leslie, Agne and Kiko.
