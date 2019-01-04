def averages():

    file = open("output.txt",'r')
    total = 0.0
    i = 0

    ranks = {
        "diamond": 0 ,#2000+
        "platinum" :0 ,#1679-1999
        "gold" : 0 ,#1338-1678
        "silver" : 0 ,#1086-1337
        "bronze" : 0 ,#1086-872
        "tin" : 0 # <872
    }

    #change to switch - cases!
    for line in file:
        i += 1
        elo = int(line)

        if(elo>=2000):
            ranks["diamond"] += 1
        if(elo<2000 and elo >= 1679):
            ranks["platinum"] += 1
        if(elo<1679 and elo >=1338):
            ranks["gold"] += 1
        if(elo < 1338 and elo >= 1086):
            ranks["silver"] += 1
        if(elo < 1086 and elo >= 872):
            ranks["bronze"] += 1
        if(elo < 872):
            ranks["tin"] += 1


    file.close()

    return ranks, i