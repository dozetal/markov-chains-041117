"""Generate markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """
    
    Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and 
    Turns the file's contents as one string of text.
    
    """

    # your code goes here
    # read the file, return as text as a string titled "contents"
    contents = open(file_path).read()

    # return "Contents of your file as one long string"
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

    # Make a list of words in text_string
    words = text_string.split()

    # create dictionary
    chains = {}

    # Iterate over the index numbers of the list
    for i in range(len(words)-2):
        
        # create a tuple of two n-grams
        bigrams = (words[i], words[i+1])

        # check for repeat of keys / bigrams
        if bigrams not in chains:

            # if the key doesn't exists, add key to chains
            chains[bigrams] = [words[i+2]]

       # if bigram is in the list, append value to the type list
        else:
            chains[bigrams].append(words[i+2])


    return chains

    # Code has been revieweed and works up to this point

def make_text(chains):
    """Returns text from chains."""

    words = []

    # psuedocode

    # while t1 has VALUES 
    #     --> t2
    #         while t2 has VALUES:
    #             --> t3
    #             pass


    # Set random tuple to variable X
    x = choice(chains.keys())

    # chains[x] = choice()

    # Rnadomly choose a VALUE from a list
    word = choice(chains[x])

    # # Unpack X - a tuple - to get  
    # (key1,  key2) = x
    # print key1
    # print key2
    # Append key1, key2 and word to words
    # words.append(key1)
    # words.append(key2)

    # Append x[0], x[1]. and word to words
    words.append(x[0])
    words.append(x[1])
    words.append(word)

    return words
    # return " ".join(words)


""" 
This works for the first part. 
Next up: Loop through the rest of the dictionary
"""

# assigns greens-eggs.txt to variable
input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

print chains

# Produce random text
random_text = make_text(chains)

print random_text
