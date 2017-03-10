import pprint
import json

with open('results.json', 'r') as ts_file:
    ts = json.load(ts_file)

def print_bombo(b, idb):
    print "Teams in bombo:", idb
    for x in b:
        print(x)
    print("\n")
        

def sorteo(b1, b2, ac):
    global poss, vg
    if len(b1) == 0 and len(b2) == 0:
        vg += 1
        for a in ac:
            poss[a] += 1
        return

    w = b1.pop()
    for c in set((w, l) for l in b2 if condition(w, l)):
        b2c, acc = b2.copy(), ac.copy()
        b2c.remove(c[1])
        acc.add(c)
        sorteo(b1.copy(), b2c, acc )

# totally necessary lambda functions =D @mgomezch

bombo = lambda x: set(t for t, i in ts.items() if i['p']==x)
condition = lambda x, y: ts[x]['c'] != ts[y]['c'] and ts[x]['g'] != ts[y]['g']
tournament = lambda x,y: set((w, l) for w in x for l in y if condition(w, l))

def main():
    pp = pprint.PrettyPrinter(indent=3)
    b1, b2 = bombo(1), bombo(2)
    matches = {}

    global vg, poss

    while len(b1)>0:
        gs = tournament(b1.copy(), b2.copy())
        poss = dict()

        for g in gs:
            poss[g] = 0
        
        vg = 0

        sorteo(b1.copy(), b2.copy(), set())
            
        for g in gs:
            poss[g] = poss[g]*1.0/vg
                    
        pp.pprint(poss)
        
        print("\nSelect teams drafted by name \n")

        match = ""
        while match not in poss.keys():
            print("Select team from bombo 1")
            print_bombo(b1, "1")
            team1 = ""
            while team1 not in b1:
                team1 = raw_input()
            
            print("Select team from bombo 2")
        
            print_bombo(b2, "2")
            team2 = ""
            
            while team2 not in b2:
                team2 = raw_input()
            match = (unicode(team1), unicode(team2))        

        b1.remove(team1)
        b2.remove(team2)
        matches[(team1, team2)] = poss[match]
        print(len(b1))

    print("Matches and probabilities")
    for k, v in matches.items():
        print("%s %.2f"%(k,v))
        

if __name__ == "__main__":
    main()


        
    
    
