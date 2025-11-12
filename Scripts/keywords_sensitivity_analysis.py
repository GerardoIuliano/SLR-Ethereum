#ho una lista di file json
list_of_files = ['ICSE21.json', 'ICSE22.json', 'ICSE23.json', 'ICSE24.json', 'ICSE25.json', 
                 'FSE21.json', 'FSE22.json', 'FSE23.json', 'FSE24.json', 'FSE25.json', 
                 'ASE21.json', 'ASE22.json', 'ASE23.json', 'ASE24.json', 'ASE25.json', 
                 'ISSTA21.json', 'ISSTA22.json', 'ISSTA23.json', 'ISSTA24.json', 'ISSTA25.json',
                 'ICST21.json', 'ICST22.json', 'ICST23.json', 'ICST24.json', 'ICST25.json']


import json
from collections import Counter
import pandas as pd
import re, os

# MEV, Cross-chain bridges, Layer-2 solutions, Rollups, Optimistic Rollups, zk-Rollups, Upgradeable proxies, DeFi protocols, Oracles, Consensus vulnerabilities, Governance token bugs, DAO logic bugs, Storage collisions, Sandwich attacks, Wide and Deep Neural Networks, Graph Neural Networks, Large Language Models, LLM, Representation learning, Hybrid models, Interoperability risks, Wrapped tokens, NFT vulnerabilities, DAO governance attacks, Privacy-preserving protocols, zk-SNARKs, Mixers, AI-assisted verification, Hybrid vulnerability detection

# apri un file excel
file_path = './Replication Package/Query_results_RP.xlsx'
df = pd.read_excel(file_path, sheet_name='Conferences', header=0)
titleColumn = df['Title']
print(titleColumn)
# Inizializzo un contatore per i paper che soddisfano una query
keyword_counter = 0
keyword_counter_2 = 0
total_papers = 0
covered_papers = 0
# Definisco le keyword da cercare MEV, cross-chain bridges, Wide and Deep Neural Network, rollups, Layer-2, upgradeable proxies, DeFi protocols
keywords = ['MEV', 'Maximal Extractable Value', 'cross-chain bridges', 'Deep Neural Network', 'rollups', 'Layer-2', 'upgradeable proxies', 'DeFi protocols']
pattern = re.compile(r'^(?=.*\b(smart contract|smart contracts|Ethereum)\b)'
                     r'(?=.*\b(vulnerability|vulnerabilities|bug|bugs|security|analysis|detection|tool|verification)\b).*', re.IGNORECASE)
pattern_2 = re.compile(r'^(?=.*\b(smart contract|smart contracts|Ethereum)\b)'
                     r'(?=.*\b(vulnerability|vulnerabilities|bug|bugs|security|analysis|detection|tool|verification|MEV|Maximal Extractable Value|cross-chain bridges|Deep Neural Network|rollups|Layer-2|upgradeable proxies|DeFi protocols)\b).*',re.IGNORECASE)
pattern_3 = re.compile(
    r'^(?=.*\b(smart contract|smart contracts|Ethereum)\b)'
    r'(?=.*\b(vulnerability|vulnerabilities|bug|bugs|security|analysis|detection|tool|verification|'
    r'MEV|Cross-chain bridges|Layer-2 solutions|Rollups|Optimistic Rollups|zk-Rollups|Upgradeable proxies|'
    r'DeFi protocols|Oracles|Consensus vulnerabilities|Governance token bugs|DAO logic bugs|Storage collisions|'
    r'Sandwich attacks|Wide and Deep Neural Networks|Graph Neural Networks|Large Language Models|LLM|'
    r'Representation learning|Hybrid models|Interoperability risks|Wrapped tokens|NFT vulnerabilities|'
    r'DAO governance attacks|Privacy-preserving protocols|zk-SNARKs|Mixers|AI-assisted verification|'
    r'Hybrid vulnerability detection)\b).*',
    re.IGNORECASE
)
# Itero sui file JSON
folder = "./Stats/conferences/"
for file_name in os.listdir(folder):
    full_path = os.path.join(folder, file_name)
    #controlla se esiste il file
    try:
        with open(full_path, 'r') as file:
            pass
    except FileNotFoundError:
        print(f"File {file_name} not found. Skipping.")
        continue
    with open(full_path, 'r') as file:
        data = json.load(file)
        for paper in data["result"]["hits"]["hit"]:
            total_papers += 1
            title = paper["info"]["title"].lower()
            #check if title is in the excel file
            if title in map(str.lower, titleColumn):
                covered_papers += 1
            # Controllo se una delle keyword è presente nel titolo o nell'abstract
            if pattern.match(title):
                keyword_counter += 1
            if pattern_3.match(title):
                keyword_counter_2 += 1
            if (not pattern.match(title)) and pattern_3.match(title):
                print(f"Paper matched extended criteria but not basic: {title}")

print(f"Number of papers matching the criteria: {keyword_counter} out of {total_papers}")
print(f"Number of papers matching the extended criteria: {keyword_counter_2} out of {total_papers}")
print(f"Number of papers covered in the excel file: {covered_papers} out of {total_papers}")