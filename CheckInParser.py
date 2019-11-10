import re
from collections import defaultdict

checkins = defaultdict(list)
#sidre = re.compile(r'[a-zA-Z]\d{6,6}')
checkinre = re.compile(r'[a-zA-Z]\d{6,6}\s*#justcode@week\d+')

def parseSid(checkin):
    return checkin[0:7]

def parseWeek(checkin):
    # this has to be updated for challanges more than 10 weeks
    return checkin[-1]


def parseChallenge(line):
    ''' This functional parses the name of the challange if multiple challenges are running'''

def addCheckin(checkin):
    sid = parseSid(checkin)
    week = parseWeek(checkin)
    #This is future features when supporting multiple challanges
    #parseChallenge(checkin)
    checkins[sid].append(week)

def parseCheckin(line):
    checkinp = checkinre.search(line)
    if checkinp is not None:
        checkin = checkinp.group()
        addCheckin(checkin)

def processCheckins():
    with open('checkins.txt') as f:
        for line in f:
            parseCheckin(line)
    # there is likely a better python like way thank this
    for key, value in sorted(checkins.items()):
        print(key, sorted(value))

def main():
    processCheckins()

# main function calling
if __name__ == "__main__":
    main()