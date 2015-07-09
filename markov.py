import sys
from random import choice


class SimpleMarkovGenerator(object):

    def read_files(self, filenames):
        """Given a list of files, make chains from them.
        Half(ish) of the original first function from non-oo
        """
        text_string = ""
        for file_path in filenames:
            read_the_file = open(file_path)
            for line in read_the_file:
                text_string += line.rstrip("\n") + " "


        return text_string


    def make_chains(self, corpus):
        """Takes input text as string; stores chains.

        """

        chains = {}

            words = corpus.split()

            for i in range(len(words) - 2):
                key = (words[i], words[i + 1])
                value = words[i + 2]

                if key not in chains:
                    chains[key] = []

                chains[key].append(value)

        # your code here
        # ultimately returns a dictionary
        # stores chains (as opposed to creating them)
        # calls read_files before getting into its primary function

    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""
        key = choice(chains.keys())
        words = [key[0], key[1]]
        while key in chains:
        # Keep looping until we have a key that isn't in the chains
        # (which would mean it was the end of our original text)
        #
        # Note that for long texts (like a full book), this might mean
        # it would run for a very long time.

            word = choice(chains[key])
            words.append(word)
            key = (key[1], word)

        return " ".join(words)


if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    # we should make an instance of the class
    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x

    pass