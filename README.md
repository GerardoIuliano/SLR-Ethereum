# Repository Package

This repository contains all the data, analyses, and scripts used in the study on smart contract vulnerabilities, detection tools, and benchmark evaluation.  
It is organized into multiple folders, each corresponding to a specific stage of the research workflow.

---

## 📁 Root Files

### **Query_results.xlsx**
This file includes all papers extracted using the research strings.  
For each paper, the following data quality metrics are reported:

- **Contextual Data Quality (CDQ)** – evaluates the contextual relevance of the paper.  
- **Intrinsic Data Quality (IDQ)** – assesses the intrinsic validity and completeness of the study.  
- **Final Data Quality (FDQ)** – represents the overall evaluation used to determine whether the paper is included in the final dataset.

---

### **Data_analysis.xlsx**
This file includes only the papers that **passed the quality evaluation** (i.e., those with satisfactory FDQ values).  
All information was extracted from this set of papers using dedicated **data forms** designed to collect standardized information for subsequent analysis.

---

## 📂 Results Folder

The **`results/`** folder contains four separate files, one for each **Research Question (RQ)** defined in the study.  
Each file reports the detailed outcomes and synthesized data related to its respective RQ.

---

## 📂 Taxonomy Folder

The **`Taxonomy/`** folder contains all materials related to the construction and validation of the vulnerability taxonomy.

### **Synonyms_to_Representative.xlsx**
- Shows how representative vulnerabilities were selected for each **cluster of synonymous vulnerabilities**.
- Each cluster groups semantically equivalent or overlapping vulnerability labels identified across the analyzed studies.

### **Validation/**
This subfolder contains the results of the **four expert interviews** conducted to validate the taxonomy.  
Each interview provides feedback and adjustments that contributed to refining the taxonomy structure and naming.

### **TaxonomyValidation_main.xlsx**
- Summarizes the results of the expert validation process.  
- Presents a comparison between the **taxonomy before and after validation**.  
- Reports the **Cohen’s Kappa** coefficient achieved by the experts, indicating the level of agreement during the validation phase.

---

## 📂 Scripts Folder

The **`Scripts/`** folder includes all Python scripts used to process and analyze the collected data.

### **keywords_sensitivity_analysis.py**
- Evaluates the **sensitivity of the research strings** against emerging keywords.
- Helps assess whether additional or alternative keywords could improve recall in future literature searches.

### **tool_x_bench_coverage.py**
- Analyzes the **coverage of detection tools** and **benchmarks**, correlating them to measure how effectively existing tools are tested across different benchmark datasets.



