word = "Count letters in a string"
counter = {}
word = word.lower()

for c in word:
    if c != " ":
        if c not in counter:
            counter[c] = 0
        counter[c] += 1


for key in sorted(counter.keys()):
    print("'{0}' or '{1}': {2}".format(key.upper(), key, counter[key]))



para = "method adds element(s) to the dictionary if the key is not in the dictionary. " \
       "If the key is in the dictionary, it updates the key with the new value. 1235"

counter.clear()
para = para.lower()
words = para.split(" ")


for w in words:
    if w != " ":
        if w not in counter:
            counter[w] = 0
        counter[w] += 1


for key in sorted(counter.keys()):
    print("'{}': {}".format(key, counter[key]))


forbidden = "heidi"
newspiece = "asdfhwerertiasdflkrmt"
ind = 0

for c in newspiece:
    if ind >= len(forbidden):
        break
    if forbidden[ind] == c:
        ind += 1
if ind < len(forbidden):
    print("NO")
else:
    print("YES")