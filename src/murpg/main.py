from murpg.roll import Roll

roll = Roll([(4, 0), (1, 1), (1, 2)])


results = {}


for _ in range(1, 1000000):
    val = roll.roll()
    results[val] = results.get(val, 0) + 1


print(results)
