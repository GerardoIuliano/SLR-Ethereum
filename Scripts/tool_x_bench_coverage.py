import pandas as pd

covered_by_benchmark = ["1A1", "1B", "1B1", "1B2", "1D", "2A1", "2A2", "2B", "2B1", "2C", "3A", "3B1", "3C", "1J", "4I", "4D", "5A1", "5B5", "5B", "5B1", "5B2", "5C3", "6A", "7I", "8A"]

#apri un file excel
file_path = '../Data_analysis.xlsx'
df = pd.read_excel(file_path, sheet_name='RQ3_Mapping', header=2)
all = df.iloc[0]
all = all[6:]
all = all.index.tolist()
#seleziona la riga 166
coverageColumn = df.iloc[163]
#seleziona solo le colonne dalla 7 in poi
coverageColumn = coverageColumn[6:]
#stampa solo gli headers delle colonne coverageColumn
# Filtra le colonne con valore 0 e stampa i loro header
notCoveredByTool = coverageColumn[coverageColumn == 0].index.tolist()
coveredByTool = coverageColumn[coverageColumn > 0].index.tolist()
notCoveredByBenchmark = set(all) - set(covered_by_benchmark)
print("Not covered by benchmark:")
print(len(notCoveredByBenchmark))
print(notCoveredByBenchmark)
print("Covered by benchmark:")
print(len(covered_by_benchmark))
print(covered_by_benchmark)
print("Not covered by tool:")
print(len(notCoveredByTool))
print(notCoveredByTool)
print("Covered by tool:")
print(len(coveredByTool))
print(coveredByTool)

#calcola l'intersezione tra notCoveredByTool e notCoveredByBenchmark
intersection = set(notCoveredByTool) & set(notCoveredByBenchmark)
print("Intersection between not covered by tool and not covered by benchmark:")
print(len(intersection))
print(intersection)