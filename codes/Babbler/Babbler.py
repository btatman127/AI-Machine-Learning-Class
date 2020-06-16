from collections import defaultdict
from random import choices


class Babbler:
    # initializer
    def __init__(self, n, filename):
        self.n = n
        with open(filename, encoding='utf8') as file:
            text = file.read().lower().replace('\n', ' ')
        self.text = text
        self.counts = defaultdict(lambda: defaultdict(int))
        for x in range(len(text) - n):
            # finds amount of times a char follows a char string of n length
            self.counts[text[x:x + n]][text[x + n]] = self.counts[text[x:x + n]][text[x + n]] + 1

    def babble(self, word, length):
        t = word[0:self.n]
        # starts at len(t) to length to make sures t has length characters when loop is done
        for a in range(len(t), length):
            # adds next char after last n if found
            try:
                # chooses randomly from list (weighted by how many times it happens) and adds it to t
                t = t + choices(list(self.counts[t[a - self.n:a + self.n]].keys()),
                                weights=list(self.counts[t[a - self.n:a + self.n]].values()))[0]
            # if next char not found...
            except IndexError:
                # chooses randomly from text
                t = t + choices(list(self.text))[0]
        return t


# example code


# choose intelligence and text file
# "intelligence" is how many char the system looks at when choosing the next character
# s = Babbler(1, 'short.txt')

# print dictionary
# print(s.counts)

# choose starting string and output string length
# print(s.babble('t', 10))


# m = Babbler(10, 'moby.txt')
# print(m.babble('call me ishmael. some years ago', 150))
