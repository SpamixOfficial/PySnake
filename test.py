import json

tmphigh = []
with open("assets/config.json") as file:
    data = json.load(file)

def new_highscore(score=6):
    global data
    index = 0
    for section in data['highscore']:
        if score >= section:
            return index
            break
        index += 1
    return None

isnewh = new_highscore(score=24)
if not isnewh == None:
    print(data['highscore'])
    for i in range(0, 5):
        tmphigh.append(data['highscore'][i])
    del tmphigh[4]
    for i in range(isnewh, 3):
        tmphigh[i + 1] = data['highscore'][i]
    tmphigh.append(data['highscore'][3])
    tmphigh[isnewh] = 24
    print(tmphigh)
    data['highscore'] = tmphigh
    with open('assets/config.json', 'w') as file:
        json.dump(data, file, indent=4)
