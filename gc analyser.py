def read_fasta(filename):
    sequences = {}
    name = ""
    dna = ""

    for line in open(filename):
        line = line.strip()

        if line.startswith(">"):
            if name != "":
                sequences[name] = dna
            name = line[1:]
            dna = ""
        else:
            dna = dna + line

    sequences[name] = dna
    return sequences


def gc_percent(sequence):
    g = sequence.count("G")
    c = sequence.count("C")
    return (g + c) / len(sequence) * 100


def at_percent(sequence):
    a = sequence.count("A")
    t = sequence.count("T")
    return (a + t) / len(sequence) * 100


def melting_temperature(sequence):
    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")
    return 2 * (a + t) + 4 * (g + c)


data = read_fasta("sequences.fasta")

for name, seq in data.items():
    print("\nSequence name:", name)
    print("Length:", len(seq))
    print("GC %:", round(gc_percent(seq), 2))
    print("AT %:", round(at_percent(seq), 2))
    print("Melting Temperature:", melting_temperature(seq), "°C")
