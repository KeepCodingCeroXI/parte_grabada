from dices import *

rolls = {}
for roll in range(1000):
    result = sum(dices_launch(6, 2))
    if result in rolls:
        rolls[result] += 1
    else:
        rolls[result] = 1
        
keys = sorted(rolls.keys())

for v in keys:
    points = '.' * (rolls[v] // 10)
    print("{:>2d}: {:>3d}\t{}".format(v, rolls[v], points))
    