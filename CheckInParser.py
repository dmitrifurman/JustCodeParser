import re

checkins = dict()
read_data = []
sidre = re.compile(r'[a-zA-Z]\d{6,6}')
checkinre = re.compile(r'[a-zA-Z]\d{6,6}\s*#justcode\d+')

def parseSid(line):
    sidp = sidre.search(line);
    print(sidp)
    if sidp is not None:
        return sidp.group()



def parseLine(line):
    print(line)
    sid = parseSid(line)
    print(sid)


with open('checkins.txt') as f:
    for line in f:
        parseLine(line)