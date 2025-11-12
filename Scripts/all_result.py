import pandas as pd

sheets = ["Scholar", "DL_snowball", "ACM_DL", "IEEE_Xplore", "Science_Direct", "TU_Wien_CatalogPlus", "Conferences", "Paper_forward_snowball"]
columns = ["SLR", "Survey", "PS"]
rows = [
        "Journal Article",
        "Conference Proceeding or Workshop",
        "Book Section",
        "Arxiv Paper or Preprint",
        "Thesis or Seminar Paper",
        "Technical Report"]

df_result = pd.DataFrame(columns=columns, index=rows)
df_result = df_result.fillna(0)
 
paper_set = set()
duplicate = 0

for sheet in sheets:
    file = pd.read_excel("../Query_results.xlsx", sheet) 
    print(sheet, len(file))
    for index, row in file.iterrows():
        if paper_set.__contains__(row["Title"]):
            duplicate += 1
        else:
            paper_set.add(row["Title"])

print("duplicate", duplicate)
print( len(paper_set))
print(len(paper_set)+duplicate)
