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
    kvinnocounter = 0 #counts absolute numbers of names
    kvinnonamnfrekvens = {} #counts unique names
    for t in text:
        if t in kvinnodict:
            kvinnonamnfrekvens[t] = kvinnodict[t]
            kvinnocounter += 1
    return(kvinnonamnfrekvens, kvinnocounter)

def raknamaen():
    maencounter = 0
    maennamnfrekvens = {}
    for t in text:
        if t in maendict:
            maennamnfrekvens[t] = maendict[t]
            maencounter += 1
    return(maennamnfrekvens, maencounter)

#Launch the functions
kvinnorslutresultat = raknakvinnor()
maenslutresultat = raknamaen()

#Print the names
for keys, values in kvinnorslutresultat[0].items():
    print("\t" + keys, values)
for keys, values in maenslutresultat[0].items():
    print("\t" + keys, values)

#Print again at bottom of screeen
print("Det finns " + str(len(kvinnorslutresultat[0])) + " unika kvinnonamn i texten.")
print("Det finns " + str(len(maenslutresultat[0])) + " unika mansnamn i texten.")

print("Absoluta tal kvinnor: " + str(kvinnorslutresultat[1]))
print("Absoluta tal män: " + str(maenslutresultat[1]))
