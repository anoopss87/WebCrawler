

def formatter(table):
    file = open('urllist.txt', 'r')

    for line in file:
        words = line.split(',')
        table[words[1]] = words[0]


def prformatter(table):
    file = open('pagerank.txt', 'r')

    out = open('prank.txt', 'w+')
    for line in file:
        words = line.split(' ')
        if table.get(words[1]) is not None:
            out.write(words[0] + " " + str(table.get(words[1])) + "\n")
        else:
            print words[1]


if __name__ == "__main__":
    table = dict()
    formatter(table)
    prformatter(table)