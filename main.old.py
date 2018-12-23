import json, math

loadpath = './data/2017-01-09_dickson.json'

with open(loadpath) as file:
    filecontents = file.read()
    # print(filecontents)
data = json.loads(filecontents)

candidates = data['candidates']
votes      = data['votes']

for candidate in candidates:
    candidate['votes'] = []
    for i in range(len(candidates)):
        candidate['votes'].append(0)

# Count votes and allocate preferences to candidates
for vote in votes:
    pref_num = 0
    for pref in vote:
        pref_num += 1
        for candidate in candidates:
            if candidate['id'] == pref:
                candidate['votes'][pref_num - 1] += 1

minVotes = math.inf
for candidate in candidates:
    if candidate['votes'][0] < minVotes:
        minVotes = candidate['votes'][0]

# for candidate in candidates:
#     if 


print(candidates)
