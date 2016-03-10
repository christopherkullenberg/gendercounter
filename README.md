# Gendercounter
A program for counting the occurrence of male and female Swedish names in a text file.

Try the live web version: [genuskollen.se](http://genuskollen.se)


## Functionality
A series of functions for counting gendered Swedish names in text.
Import the gendercounter.py script along with the tsv files containing names and frequencies:

    female250.tsv
    male250.tsv

Then you can:

    import gendercounter

Consequently, the following function will take text as input:

    gendercounter.textinput('Hej hen heter Lisa eller Kalle')

Which will return the result as tuples and dictionaries like so:

    (({'Lisa': '31611'}, 1), ({'Kalle': '2903'}, 1), (1, 0, 0), (0, 0, 0), (0, 0, 0))

The first two dictionaries list female and male names respectively, along with the frequency of occurrence according to Statistics Sweden (2015). The tuples contain the pronouns hen/hon/han according to the following variations.

1. hen/henom/hens
2. hon/henne/hennes
3. han/honom/hans


## Usage as a script
Take the lines that have been commented out and comment them back in. Ten run:

    python3 gendercounter.py file.txt

## Sources of error
- Some names are also frequent Swedish words, for example "De".
- Uncommon names (less than 250 occurrences) were excluded.
- Some names are gender neutral ("Charlie", "Mario", "Alex" etc.)
- With the pronoun counter, the words "Han" and "Hans" can also be Swedish male names.
- ??? (Please let me know if you find other sources of error)

## Removed names
- "De"
- "Del"

## Similar programs
* [SexMachine](https://pypi.python.org/pypi/SexMachine/) (English language, written in Python)
