
import itertools

count = 0

valid_digits = [ 'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg' ]

def transform(mapping, word):
    output = ""

    for letter in word:
        output = output + (mapping[ord(letter) - ord('a')])

    return "".join(sorted(output))

def list_to_number_base_10(list):
    return int("".join([ str(x) for x in list ]))

with open("Input.txt") as file:
    for line in file:
        inputs = line.split("|")[0].split()
        outputs = line.split("|")[1].split()

        for mapping in itertools.permutations('abcdefg'):
            if all(( transform(mapping, x) in valid_digits for x in inputs )):
                count = count + list_to_number_base_10([ valid_digits.index(transform(mapping, x)) for x in outputs ])

print(count)