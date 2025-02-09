from aocd import get_data

passphrases = [
    ["".join(sorted(word)) for word in line.strip().split(" ")]
    for line in get_data(year=2017, day=4).splitlines()
]

print(sum(len(passphrase) == len(set(passphrase)) for passphrase in passphrases))
