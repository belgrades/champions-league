import pprint
import json

with open('results.json', 'r') as ts_file:
    ts = json.load(ts_file)

vg = 0	
poss = dict()

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
    gs = tournament(b1, b2)

    for g in gs:
        poss[g] = 0
            
    sorteo(b1, b2, set())
            
    for g in gs:
        poss[g] = poss[g]*1.0/vg
                    
    pp.pprint(poss)
    print(vg)

if __name__ == "__main__":
    main()


        
    
    
