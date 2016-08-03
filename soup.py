import urllib
from bs4 import BeautifulSoup


def getText(url, name):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')

    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out

    out_file = open("webText/" + name, 'w+')
    text = soup.get_text('|', strip =True)
    lines = text.split('|')
    for line in lines:
        cleanLine = line.encode('ascii', 'replace').replace('?', ' ')
        cleanLine = cleanLine.replace(",", " ").replace("(", "").replace(")", "")
        if cleanLine.strip():
            out_file.write(cleanLine + "\n")
    out_file.close()

if __name__ == "__main__":
    list = open('urllist.txt', 'r')

    for line in list:
        words = line.split(',')
        getText(words[1], words[0])