# This script will contain data analysis functions for the replication package.

import pandas as pd
import numpy as np
from collections import Counter

# Define your data analysis functions here
def analyze_data(file_path, sheet_name, header):
    """
    Function to analyze data from the given file path and sheet name.
    """
    # Load the specified sheet into a DataFrame using the specified header row
    data = pd.read_excel(file_path, sheet_name=sheet_name, header=header)
    return data

# Example usage
def method_x_vulnerability():
    
    """Analyze which vulnerabilities are addressed by tools using specific methods."""

    file_path = '../Data_analysis.xlsx'
    
    # Load the RQ2_Tools sheet
    sheet_name = 'RQ2_Tools'
    final_tools_df = analyze_data(file_path, sheet_name, header=3)
    
    # Load the RQ3_Mapping sheet
    sheet_name = 'RQ3_Mapping'
    final_mapping_df = analyze_data(file_path, sheet_name, header=2)
    
    # Perform a join on the 'Tool' column
    merged_df = pd.merge(final_tools_df, final_mapping_df, on='Tool', how='inner')
    
    # List of methods
    methods = [
        "Symbolic Execution", "Formal Verification and Constraint Solving", "Model Checking",
        "Abstract Interpretation", "Fuzzing", "Runtime Verification", "Concoli Testing",
        "Mutation testing (method)", "Pattern Matching/ Rule-Based", "Code Instrumentation (ALGO)",
        "Machine Learning/ Deep Learning/ AI", "Taint Analysis"
    ]
    
    # Iterate over each method and perform the analysis
    for method_column in methods:
        if method_column in merged_df.columns:
            # Filter tools that use the specified method with the value ✓
            tools_using_method = merged_df[merged_df[method_column] == '✓']
            
            # Check columns from index 47 onwards for ✓ and save headers in a list
            relevant_columns = merged_df.columns[45:]  # Select columns from index 47 onwards
            
            method_columns = {}
            
            for index, row in tools_using_method.iterrows():
                tool_name = row['Tool']
                method_columns[tool_name] = [
                    col for col in relevant_columns if row[col] == '✓'
                ]
            
            # Count the frequency of column headers and sort in descending order
            all_columns = []
            for tool, columns in method_columns.items():
                all_columns.extend(columns)
            
            column_frequency = Counter(all_columns)
            # print(f"Top 10 vulnerabilities addressed using {method_column}:")
            top_10 = column_frequency.most_common(10)
            
            # Format the output as "method, column (frequency), column (frequency), ..."
            formatted_output = f"{method_column}, " + ", ".join([f"{column} ({frequency})" for column, frequency in top_10])
            print(formatted_output)

def method_x_input():
    
    """Analyze which vulnerabilities are addressed by tools using specific methods."""

    file_path = '../Data_analysis.xlsx'
    
    # Load the RQ2_Tools sheet
    sheet_name = 'RQ2_Tools'
    final_tools_df = analyze_data(file_path, sheet_name, header=3)
    
    # Load the RQ3_Mapping sheet
    sheet_name = 'RQ3_Mapping'
    final_mapping_df = analyze_data(file_path, sheet_name, header=2)
    
    # Perform a join on the 'Tool' column
    merged_df = pd.merge(final_tools_df, final_mapping_df, on='Tool', how='inner')
    
    # List of methods
    methods = [
        "Symbolic Execution", "Formal Verification and Constraint Solving", "Model Checking",
        "Abstract Interpretation", "Fuzzing", "Runtime Verification", "Concoli Testing",
        "Mutation testing (method)", "Pattern Matching/ Rule-Based", "Code Instrumentation (ALGO)",
        "Machine Learning/ Deep Learning/ AI", "Taint Analysis"
    ]
    
    # Iterate over each method and perform the analysis
    for method_column in methods:
        if method_column in merged_df.columns:
            # Filter tools that use the specified method with the value ✓
            tools_using_method = merged_df[merged_df[method_column] == '✓']
            
            # Check columns from index 47 onwards for ✓ and save headers in a list
            relevant_columns = merged_df.columns[10:12]  # Select columns from index 47 onwards
            
            method_columns = {}
            
            for index, row in tools_using_method.iterrows():
                tool_name = row['Tool']
                method_columns[tool_name] = [
                    col for col in relevant_columns if row[col] == '✓'
                ]
            
            # Count the frequency of column headers
            all_columns = []
            for tool, columns in method_columns.items():
                all_columns.extend(columns)
            
            column_frequency = Counter(all_columns)
            
            # Format the output as "method, column (frequency), column (frequency), ..."
            formatted_output = f"{method_column}, " + ", ".join([f"{column} ({frequency})" for column, frequency in column_frequency.items()])
            print(formatted_output)

def method_x_ir():
    
    """Analyze which vulnerabilities are addressed by tools using specific methods."""

    file_path = '../Data_analysis.xlsx'
    
    # Load the RQ2_Tools sheet
    sheet_name = 'RQ2_Tools'
    final_tools_df = analyze_data(file_path, sheet_name, header=3)
    
    # Load the RQ3_Mapping sheet
    sheet_name = 'RQ3_Mapping'
    final_mapping_df = analyze_data(file_path, sheet_name, header=2)
    
    # Perform a join on the 'Tool' column
    merged_df = pd.merge(final_tools_df, final_mapping_df, on='Tool', how='inner')
    
    # List of methods
    methods = [
        "Symbolic Execution", "Formal Verification and Constraint Solving", "Model Checking",
        "Abstract Interpretation", "Fuzzing", "Runtime Verification", "Concoli Testing",
        "Mutation testing (method)", "Pattern Matching/ Rule-Based", "Code Instrumentation (ALGO)",
        "Machine Learning/ Deep Learning/ AI", "Taint Analysis"
    ]
    
    # Iterate over each method and perform the analysis
    for method_column in methods:
        if method_column in merged_df.columns:
            # Filter tools that use the specified method with the value ✓
            tools_using_method = merged_df[merged_df[method_column] == '✓']
            
            # Check columns from index 47 onwards for ✓ and save headers in a list
            relevant_columns = merged_df.columns[21:28]  # Select columns from index 47 onwards
            
            method_columns = {}
            
            for index, row in tools_using_method.iterrows():
                tool_name = row['Tool']
                method_columns[tool_name] = [
                    col for col in relevant_columns if row[col] == '✓'
                ]
            
            # Count the frequency of column headers and sort in descending order
            all_columns = []
            for tool, columns in method_columns.items():
                all_columns.extend(columns)
            
            column_frequency = Counter(all_columns)
            # print(f"Top 10 vulnerabilities addressed using {method_column}:")
            top_10 = column_frequency.most_common(10)
            
            # Format the output as "method, column (frequency), column (frequency), ..."
            formatted_output = f"{method_column}, " + ", ".join([f"{column} ({frequency})" for column, frequency in top_10])
            print(formatted_output)

method_x_vulnerability()
print("--------------------")
method_x_input()
print("--------------------")
method_x_ir()