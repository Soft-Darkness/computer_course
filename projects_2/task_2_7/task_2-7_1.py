files = ["seq1", "seq2", "seq3", "seq4"]
experiment_date = str('_01.01.2026')

for name in files:
   new_name = name + experiment_date + ".fasta"

   print(f"{new_name}")