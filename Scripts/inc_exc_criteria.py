import pandas as pd


sheets_step1 = ["Scholar", "ACM_DL", "IEEE_Xplore", "Science_Direct", "TU_Wien_CatalogPlus"]
sheets_step2 = ["DL_snowball", "Conferences", "Paper_forward_snowball"]
inclusion = {
    "1" : 0,
    "2" : 0,
    "3" : 0
}
exclusion = {
    "1" : 0,
    "2" : 0,
    "3" : 0,
    "4" : 0,
    "5" : 0
}
count = 0
included = 0
paper_set = set()
duplicate = 0
rows_per_sheet = {}

for sheet in sheets_step1:
    file = pd.read_excel('../Replication Package/Query_results.xlsx', sheet) 
    rows_per_sheet[sheet] = len(file)
    
    for index, row in file.iterrows():
        if paper_set.__contains__(row["Title"]):
            duplicate += 1
        else:
            paper_set.add(row["Title"])
            if pd.notna(row["Inc.Crit"]):
                included += 1
                if '1' in (str(row["Inc.Crit"])):
                    inclusion["1"] += 1
                if '2' in (str(row["Inc.Crit"])):
                    inclusion["2"] += 1
                if '3' in (str(row["Inc.Crit"])):
                    inclusion["3"] += 1
            if pd.notna(row["Exc.Crit"]):
                if '1' in (str(row["Exc.Crit"])):
                    exclusion["1"] += 1
                if '2' in (str(row["Exc.Crit"])):
                    exclusion["2"] += 1
                if '3' in (str(row["Exc.Crit"])):
                    exclusion["3"] += 1
                if '4' in (str(row["Exc.Crit"])):
                    exclusion["4"] += 1
                if '5' in (str(row["Exc.Crit"])):
                    exclusion["5"] += 1
            if (not (pd.notna(row["Inc.Crit"])) and not (pd.notna(row["Exc.Crit"]))):
                count += 1
print("\nStep 1")
print("\nNumber of rows per sheet:")
paper_step1=0
for sheet, rows in rows_per_sheet.items():
    print(f"{sheet}: {rows} rows")
    paper_step1 += rows
print(f"Total: {paper_step1} rows")
print("\nOther statistics:")
print("Inc",inclusion, sum(inclusion.values()))
print("Exc", exclusion, sum(exclusion.values()))
print("Included:", included)

print("Tot", count+sum(inclusion.values())+sum(exclusion.values()))
print("Duplicates:", duplicate)


inclusion = {
    "1" : 0,
    "2" : 0,
    "3" : 0
}
exclusion = {
    "1" : 0,
    "2" : 0,
    "3" : 0,
    "4" : 0,
    "5" : 0
}
count = 0

included2 = 0
duplicate = 0
rows_per_sheet = {}

for sheet in sheets_step2:
    file = pd.read_excel('../Replication Package/Query_results.xlsx', sheet) 
    rows_per_sheet[sheet] = len(file)
    
    for index, row in file.iterrows():
        if paper_set.__contains__(row["Title"]):
            duplicate += 1
        else:
            paper_set.add(row["Title"])
            if pd.notna(row["Inc.Crit"]):
                included2 += 1
                if '1' in (str(row["Inc.Crit"])):
                    inclusion["1"] += 1
                if '2' in (str(row["Inc.Crit"])):
                    inclusion["2"] += 1
                if '3' in (str(row["Inc.Crit"])):
                    inclusion["3"] += 1
            if pd.notna(row["Exc.Crit"]):
                if '1' in (str(row["Exc.Crit"])):
                    exclusion["1"] += 1
                if '2' in (str(row["Exc.Crit"])):
                    exclusion["2"] += 1
                if '3' in (str(row["Exc.Crit"])):
                    exclusion["3"] += 1
                if '4' in (str(row["Exc.Crit"])):
                    exclusion["4"] += 1
                if '5' in (str(row["Exc.Crit"])):
                    exclusion["5"] += 1
            if (not (pd.notna(row["Inc.Crit"])) and not (pd.notna(row["Exc.Crit"]))):
                count += 1
print("\nStep 2")
print("\nNumber of rows per sheet:")
paper_step1=0
for sheet, rows in rows_per_sheet.items():
    print(f"{sheet}: {rows} rows")
    paper_step1 += rows
print(f"Total: {paper_step1} rows")
print("\nOther statistics:")
print("Inc",inclusion, sum(inclusion.values()))
print("Exc", exclusion, sum(exclusion.values()))
print("Included:", included2)

print("Tot", count+sum(inclusion.values())+sum(exclusion.values()))
print("Duplicates:", duplicate)