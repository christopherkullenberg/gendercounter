from sys import argv

script, filename = argv

thefile = open(filename, 'r')
thetext = thefile.read()

#Dictionaries for names with frequency of occurrence
kvinnodict = {}
maendict = {}

#Open the name lists [0] is freq and [1] is name
with open('female250.tsv', 'r') as kvinnofile:
    kvinnor = zip((line.strip().split('\t') for line in kvinnofile))
    for row in kvinnor:
        for r in row:
            kvinnodict[r[1]] = r[0]

with open('male250.tsv', 'r') as maenfile:
    maen = zip((line.strip().split('\t') for line in maenfile))
    for row in maen:
        for r in row:
            maendict[r[1]] = r[0]

text = thetext.split()

#Two functions for counting men and women in text
def raknakvinnor():
    kvinnonamnfrekvens = {}
    for t in text:
        if t in kvinnodict:
            kvinnonamnfrekvens[t] = kvinnodict[t]
    return kvinnonamnfrekvens

def raknamaen():
    maennamnfrekvens = {}
    for t in text:
        if t in maendict:
            maennamnfrekvens[t] = maendict[t]
    return maennamnfrekvens

#Launch the functions
kvinnorslutresultat = raknakvinnor()
maenslutresultat = raknamaen()

#Print the results
print("Det finns " + str(len(kvinnorslutresultat)) + " kvinnor i texten:")
for keys, values in kvinnorslutresultat.items():
    print("\t" + keys, values)

print("Det finns " + str(len(maenslutresultat)) + " män i texten:")
for keys, values in maenslutresultat.items():
    print("\t" + keys, values)

#Print again at bottom of screeen
print("Det finns " + str(len(kvinnorslutresultat)) + " kvinnor i texten.")
print("Det finns " + str(len(maenslutresultat)) + " män i texten.")
