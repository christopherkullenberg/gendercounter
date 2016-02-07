# Gendercounter
A program for counting the occurrence of male and female Swedish names in a text file.

The script will look for name matches in the two tsv-files.

Note: This is a very early test script. I haven't figured out precisely what is going on :)


## Usage
    python3 gendercounter.py file.txt

## Sources of error
- Some names are also frequent Swedish words, for example "De".
- Uncommon names (less than 250 occurrences) were excluded.
- Some names are gender neutral ("Charlie", "Mario", "Alex" etc.)

## Removed names
- "De"
- "Del"
