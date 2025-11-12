#open excel file using pandas
import pandas as pd
import numpy as np

def idq_pre_qa():
    all_values = []  # collect everything here

    xls = pd.ExcelFile('./Replication Package/Query_results_RP.xlsx')
    for sheet in xls.sheet_names: # do not consider Info sheet
        if sheet == 'Info':
            continue
        df = pd.read_excel(xls, sheet_name=sheet)
        idq_columns = df.filter(like='IDQ')  # select IDQ columns
        
        # Apply the filter: "Exc.Crit" is empty and "Inc.Crit" is not NaN
        filtered_df = idq_columns[
            (df['Exc.Crit'].isna()) & (df['Inc.Crit'].notna())
        ]
        # select column IDQ     
        filtered_df = filtered_df.filter(like='IDQ')

        # Stack all columns into one Series using the new implementation
        stacked = filtered_df.stack(future_stack=True)
        all_values.append(stacked)

    # concatenate all stacked Series from all sheets into one long Series
    all_values_series = pd.concat(all_values, ignore_index=True)

    # turn into a DataFrame with a single column
    aggregated_df = all_values_series.to_frame(name='Aggregated_IDQ')

    # Assicurati che i dati siano numerici
    aggregated_df['Aggregated_IDQ'] = pd.to_numeric(aggregated_df['Aggregated_IDQ'], errors='coerce')

    # Calcola statistiche descrittive
    statistics = aggregated_df['Aggregated_IDQ'].describe()

    # Calcola ulteriori statistiche se necessario
    min_value = statistics['min']
    max_value = statistics['max']
    mean_value = statistics['mean']
    first_quartile = aggregated_df['Aggregated_IDQ'].quantile(0.25)
    second_quartile = aggregated_df['Aggregated_IDQ'].quantile(0.50)  # equivalente alla mediana
    third_quartile = aggregated_df['Aggregated_IDQ'].quantile(0.75)

    # Calcola il numero totale di valori
    total_values = aggregated_df['Aggregated_IDQ'].count()

    # Stampa i risultati
    print("Statistics:")
    print(f"Min: {min_value}")
    print(f"Max: {max_value}")
    print(f"Mean: {mean_value}")
    print(f"1st Quartile: {first_quartile}")
    print(f"2nd Quartile (Median): {second_quartile}")
    print(f"3rd Quartile: {third_quartile}")
    print(f"Total Values: {total_values}")


def idq_post_qa():
    all_values = []  # collect everything here

    xls = pd.ExcelFile('./Replication Package/Data_analysis_RP.xlsx')
    for sheet in xls.sheet_names: # do not consider Info sheet
        if sheet != 'Papers':
            continue
        df = pd.read_excel(xls, sheet_name=sheet)
        # select from 0 row to row 223
        df = df.iloc[0:225, :]
        idq_columns = df.filter(like='IDQ')  # select IDQ columns
        
        # Apply the filter: "Exc.Crit" is empty and "Inc.Crit" is not NaN
        filtered_df = idq_columns[
            (df['Exc.Crit'].isna()) & (df['Inc.Crit'].notna())
        ]
        # select column IDQ     
        filtered_df = filtered_df.filter(like='IDQ')

        # Stack all columns into one Series using the new implementation
        stacked = filtered_df.stack(future_stack=True)
        all_values.append(stacked)

    # concatenate all stacked Series from all sheets into one long Series
    all_values_series = pd.concat(all_values, ignore_index=True)

    # turn into a DataFrame with a single column
    aggregated_df = all_values_series.to_frame(name='Aggregated_IDQ')

    # Assicurati che i dati siano numerici
    aggregated_df['Aggregated_IDQ'] = pd.to_numeric(aggregated_df['Aggregated_IDQ'], errors='coerce')

    # Calcola statistiche descrittive
    statistics = aggregated_df['Aggregated_IDQ'].describe()

    # Calcola ulteriori statistiche se necessario
    min_value = statistics['min']
    max_value = statistics['max']
    mean_value = statistics['mean']
    first_quartile = aggregated_df['Aggregated_IDQ'].quantile(0.25)
    second_quartile = aggregated_df['Aggregated_IDQ'].quantile(0.50)  # equivalente alla mediana
    third_quartile = aggregated_df['Aggregated_IDQ'].quantile(0.75)

    # Calcola il numero totale di valori
    total_values = aggregated_df['Aggregated_IDQ'].count()

    # Stampa i risultati
    print("Statistics:")
    print(f"Min: {min_value}")
    print(f"Max: {max_value}")
    print(f"Mean: {mean_value}")
    print(f"1st Quartile: {first_quartile}")
    print(f"2nd Quartile (Median): {second_quartile}")
    print(f"3rd Quartile: {third_quartile}")
    print(f"Total Values: {total_values}")


idq_pre_qa()
idq_post_qa()