#!/usr/bin/env python3
# make_variants.py -- generates variants.tsv and samples.tsv
import random

random.seed(20260923)

chroms = {"chr1": 24_000_000, "chr2": 18_000_000, "chrZ": 9_000_000, "chrMT": 17_000}
genes = ["MC1R", "ASIP", "TYR", "SLC45A2", "AGRP", "KITLG", "EDNRB", "PMEL", "."]
effects = ["missense", "synonymous", "intergenic", "intron", "stop_gained", "splice"]
bases = "ACGT"

with open("variants.tsv", "w") as out:
    out.write("chrom\tpos\tref\talt\tqual\tdepth\tmaf\tgene\teffect\n")
    rows = []
    for chrom, size in chroms.items():
        n = {"chr1": 800, "chr2": 600, "chrZ": 450, "chrMT": 150}[chrom]
        for _ in range(n):
            ref = random.choice(bases)
            alt = random.choice([b for b in bases if b != ref])
            qual = round(random.choice([random.uniform(2, 28), random.uniform(30, 99)]), 1)
            depth = random.choice([random.randint(2, 9), random.randint(10, 120)])
            maf = round(random.uniform(0.005, 0.5), 4)
            eff = random.choice(effects)
            gene = "." if eff == "intergenic" else random.choice(genes[:-1])
            rows.append((chrom, random.randint(1000, size), ref, alt,
                         qual, depth, maf, gene, eff))
    for r in sorted(rows, key=lambda x: (x[0], x[1])):
        out.write("\t".join(map(str, r)) + "\n")

with open("samples.tsv", "w") as out:
    out.write("sample_id\tspecies\tpopulation\tcoverage\n")
    for i, (sp, pop) in enumerate(
        [("Colinus_virginianus", "Louisiana")] * 8
        + [("Colinus_virginianus", "Texas")] * 7
        + [("Colinus_nigrogularis", "Yucatan")] * 5, 1):
        out.write(f"BOB{i:03d}\t{sp}\t{pop}\t{round(random.uniform(4, 35), 1)}\n")
