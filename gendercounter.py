#!/usr/bin/env python3
#from sys import argv
import re

def parse(string):
    textsplit = string.split()
    text = []
    # This loop removes special chars from each word.
    for t in textsplit:
        tclean = re.sub(r'[.,\?!]+',r'',t)
        text.append(tclean)
    return(text)

def loadkvinnodict():
    kvinnodict = {}
    with open('female250.tsv', 'r', encoding='utf-8') as kvinnofile:
        kvinnor = zip((line.strip().split('\t') for line in kvinnofile))
        for row in kvinnor:
            for r in row:
                kvinnodict[r[1]] = r[0]
    return kvinnodict

def loadmaendict():
    maendict = {}
    with open('male250.tsv', 'r', encoding='utf-8') as maenfile:
        maen = zip((line.strip().split('\t') for line in maenfile))
        for row in maen:
            for r in row:
                maendict[r[1]] = r[0]
    return(maendict)

class from_string:
    '''Explanation...'''

    def __init__(self, string):
        self.text = parse(string)
        self.kvinnodict = loadkvinnodict()
        self.maendict = loadmaendict()


    def raknakvinnor(kvinnodict, text):
        kvinnofrom_stringer = 0 #from_strings absolute numbers of names
        kvinnonamnfrekvens = {} #from_strings unique names
        for t in text:
            if t in kvinnodict:
                kvinnonamnfrekvens[t] = kvinnodict[t]
                kvinnofrom_stringer += 1
        return(kvinnonamnfrekvens, kvinnofrom_stringer)

    def raknamaen(maendict, text):
        maenfrom_stringer = 0
        maennamnfrekvens = {}
        for t in text:
            if t in maendict:
                maennamnfrekvens[t] = maendict[t]
                maenfrom_stringer += 1
        return(maennamnfrekvens, maenfrom_stringer)

    def raknahen(text):
        hen = 0
        henom = 0
        hens = 0
        for t in text:
            henregexp = re.findall(r'\bhen\b', t, flags = re.IGNORECASE)
            henomregexp = re.findall(r'\bhenom\b', t, flags = re.IGNORECASE)
            hensregexp = re.findall(r'\bhens\b', t, flags = re.IGNORECASE)
            if henregexp:
                hen += 1
            elif henomregexp:
                henom += 1
            elif hensregexp:
                hens += 1
            else:
                continue
        return(hen, henom, hens)

    def raknahon(text):
        hon = 0
        henne = 0
        hennes = 0
        for t in text:
            honregexp = re.findall(r'\bhon\b', t, flags = re.IGNORECASE)
            henneregexp = re.findall(r'\bhenne\b', t, flags = re.IGNORECASE)
            hennesregexp = re.findall(r'\bhennes\b', t, flags = re.IGNORECASE)
            if honregexp:
                hon += 1
            elif henneregexp:
                henne += 1
            elif hennesregexp:
                hennes += 1
            else:
                continue
        return(hon, henne, hennes)

    def raknahan(text):
        han = 0
        honom = 0
        hans = 0
        for t in text:
            hanregexp = re.findall(r'\bhan\b', t, flags = re.IGNORECASE)
            honomregexp = re.findall(r'\bhonom\b', t, flags = re.IGNORECASE)
            hansregexp = re.findall(r'\bhans\b', t, flags = re.IGNORECASE)
            if hanregexp:
                han += 1
            elif honomregexp:
                honom += 1
            elif hansregexp:
                hans += 1
            else:
                continue
            return(han, honom, hans)

    def genderfrequency(self):
        kvinnorslutresultat = from_string.raknakvinnor(self.kvinnodict, self.text)
        maenslutresultat = from_string.raknamaen(self.maendict, self.text)
        result = {}
        result["Women"] = kvinnorslutresultat[1]
        result["Men"] = maenslutresultat[1]
        return(result)

    def pronounfrequency(self):
        henslutresultat = from_string.raknahen(self.text)
        honslutresultat = from_string.raknahon(self.text)
        hanslutresultat = from_string.raknahan(self.text)
        result = {}
        result["hen"] = henslutresultat[0]
        result["henom"] = henslutresultat[1]
        result["hens"] = henslutresultat[2]
        result["hon"] = honslutresultat[0]
        result["henne"] = honslutresultat[1]
        result["hennes"] = honslutresultat[2]
        result["han"] = hanslutresultat[0]
        result["honom"] = hanslutresultat[1]
        result["hans"] = hanslutresultat[2]
        return(result)

class from_textfile(from_string):
    def __init__(self, string):
        textfile = open(string, encoding="utf-8")
        text = textfile.read()
        self.text = parse(text)
        self.kvinnodict = loadkvinnodict()
        self.maendict = loadmaendict()  

    """explanation"""
