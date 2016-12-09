# champions-league
Code to calculate the probability of every possible match in the Round of 16 given tournament conditions

A game g between teams x and y is valid iff:

1. x and y are not from the same country.
1. x and y did'nt play in the same group.

## Dumb implementation with combinatorics

```python
# All posible matches with group condition and country condition
games = set((w, l) for w in x for l in y if ts[w]['c'] != ts[l]['c'] and ts[w]['g'] != ts[l]['g'])

# For each possible subset of size 8 inside the 47 possible games
for comb in combinations(games, 8):
    size += 1
    teams = set()
    
    # If a team repeats, then is not valid
    for k, v in comb:
        if k in teams:
            break
        if v in teams:
            break
        teams.add(k)
        teams.add(v)

    # A subset comb is valid iff it has size 16    
    if len(teams)==16:
        valid_games += 1
        for game in comb:
            poss[game] += 1
```

## Better (faster) implementation using a (naive) BT:

```python
# b1 and b2 representes the sets of winners and runners-up of group stage.
def sorteo(b1, b2, ac):
    global poss, vg
    
    # return condition both sets are empty. Update occurrence for match a in ac.
    if len(b1) == 0 and len(b2) == 0:
        vg += 1
        for a in ac:
            poss[a] += 1
        return

    # Choose a random winner in b1, for all l such that (w,l) is a valid game call sorteo with
    # sorteo(b1 - w, b2 - l, ac.union((w, l)) for all l in valids(w, l)
    w = b1.pop()
    for c in set((w, l) for l in b2 if condition(w, l)):
        b2c, acc = b2.copy(), ac.copy()
        b2c.remove(c[1])
        acc.add(c)
        sorteo(b1.copy(), b2c, acc)
```
