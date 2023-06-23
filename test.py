import json

tmphigh = []
with open("assets/stats.json") as file:
    data = json.load(file)

def new_highscore(score=6):
    global data
    index = 0
    for section in data['highscore'].values():
        if score >= section:
            return index
            break
        index += 1
    return None

isnewh = new_highscore(score=4)
highscoredata = data['highscore'].values()
highscoredata = list(highscoredata)
print(highscoredata)
print(isnewh)
if not isnewh == None:
    print(data['highscore'])
    for i in range(0, 5):
        tmphigh.append(highscoredata[i])
    del tmphigh[4]
    for i in range(isnewh, 3):
        tmphigh[i + 1] = highscoredata[i]
    tmphigh.append(highscoredata[3])
    tmphigh[isnewh] = 4
    print(tmphigh)
    i = 0
    del data['highscore'][list(data['highscore'].keys())[4]]
    for section in list(data['highscore'].keys()):
        data['highscore'][section] = tmphigh[i]
        i += 1
    data['highscore']["Alex"] = tmphigh[4]
    print(data['highscore'])
    #data['highscore'] = tmphigh
    #with open('assets/config.json', 'w') as file:
    #    json.dump(data, file, indent=4)
