from random import randint

players = {
    1:"Puneet",
    2:"Robin",
    3:"Andreas",
    4:"Gabriel",
    5:"Tim"
}

matches =[]
match_no = 1

if len(players)%2 != 0:
    players[len(players)+1] = 'Blank'

n = len(players)

for i in range (n):
    for x in range (n-1):
        if i < x+1:
            matches.append("%s-%s" % (players[i+1],players[x+2]))

while match_no<=len(matches):
    x = randint(0,len(matches)-1)
    if matches[x] != "scheduled":
        print("\n++++++ Match %s +++++\n %s\n" % (match_no, matches[x]))
        match_no += 1
        matches[x] = "scheduled"
