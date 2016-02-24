from sys import argv
import re

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
    for t2 in text:
        if t2 in maendict:
            maennamnfrekvens[t2] = maendict[t2]
            maencounter += 1
    return(maennamnfrekvens, maencounter)

def raknahen():
    hen = 0
    henom = 0
    hens = 0
    for t3 in text:
        henregexp = re.findall(r'\bhen\b', t3, flags = re.IGNORECASE)
        henomregexp = re.findall(r'\bhenom\b', t3, flags = re.IGNORECASE)
        hensregexp = re.findall(r'\bhens\b', t3, flags = re.IGNORECASE)
        if henregexp:
            hen += 1
        elif henomregexp:
            henom += 1
        elif hensregexp:
            hens += 1
        else:
            continue
    return(hen, henom, hens)

def raknahon():
    hon = 0
    henne = 0
    hennes = 0
    for t4 in text:
        honregexp = re.findall(r'\bhon\b', t4, flags = re.IGNORECASE)
        henneregexp = re.findall(r'\bhenne\b', t4, flags = re.IGNORECASE)
        hennesregexp = re.findall(r'\bhennes\b', t4, flags = re.IGNORECASE)
        if honregexp:
            hon += 1
        elif henneregexp:
            henne += 1
        elif hennesregexp:
            hennes += 1
        else:
            continue
    return(hon, henne, hennes)

def raknahan():
    han = 0
    honom = 0
    hans = 0
    for t5 in text:
        hanregexp = re.findall(r'\bhan\b', t5, flags = re.IGNORECASE)
        honomregexp = re.findall(r'\bhonom\b', t5, flags = re.IGNORECASE)
        hansregexp = re.findall(r'\bhans\b', t5, flags = re.IGNORECASE)
        if hanregexp:
            han += 1
        elif honomregexp:
            honom += 1
        elif hansregexp:
            hans += 1
        else:
            continue
    return(han, honom, hans)


#Launch the functions
kvinnorslutresultat = raknakvinnor()
maenslutresultat = raknamaen()
henslutresultat = raknahen()
honslutresultat = raknahon()
hanslutresultat = raknahan()

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
print("Antalet hen, henom, hens : " + str(henslutresultat))
print("Antalet hon, henne, hennes : " + str(honslutresultat))
print("Antalet han*, honom, hans* : " + str(hanslutresultat))
print('Obs: "Han" och "Hans" kan också vara manliga förnamn.')
