from mpmath import mp

mp.dps = 100000
pi = str(mp.pi)[2:]

searchLen = 11
searchValue = '00011122233'

for i in range(len(pi) - searchLen):
    number = pi[i : i + searchLen]
    if searchValue == number:
        print('found, index:', i)
        print(number)
