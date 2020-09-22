addict = {'A': ['B', 'C'],
          'B': ['E','A'],
          'C': ['E','A', 'B','F']}

sorted_keys = addict.keys()
size = len(sorted_keys)

for i in range(len(sorted_keys)):
    for j in addict[i]:
        print(i,j)
