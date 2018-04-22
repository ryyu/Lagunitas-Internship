# Ryan Yu
# 04/20/2018
# python 2.7

from collections import Counter


def main():

    text = raw_input("Enter a song quote or some text: ")
    textList = text.split()

    # uses the counter structure from the collections library.
    # this allows you to easily hash and count up instances of
    # unique data. Data is stored as key:value pairs.
    # Keys are case sensitive.
    wordCount = Counter()

    for word in textList:
        wordCount[word] += 1

    print wordCount


main()
