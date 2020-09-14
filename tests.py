x = input()
g = 50
if (len(x) % 2) == 1:
    g += 1

print(('{0:*<' + str(g) + '}').format(x))