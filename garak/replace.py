import sys

command = sys.argv[1]
print(command)
with open('probes.txt', 'r') as file:
    with open('new.sh', 'w') as w:
        for f in file:
            if '🌟' in f:
                probename = f[21:].split(' ')[0]
                w.write(command+" "+probename+"\n")