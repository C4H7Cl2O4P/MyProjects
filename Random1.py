import random
qestions = ["who I am?", "where I am?"]
random.shuffle(qestions)
amswers = ["You don't want to know it", "I can't answer exactly"]
random.shuffle(amswers)
for item in range(2):
    print("_________________________")
    print(str (item + 1) + ":")
    print("Q: Hey, someone " + qestions[item] + "\n")
    print("Voice: " + amswers[item] + "\n")
