import pandas as pd
import os 
import pickle

def analyze_file(file_path):
    ext = file_path.split(".")[-1].lower()

    if ext == "csv":
        df = pd.read_csv(file_path)
    elif ext in ["xlsx", "xls"]:
        df = pd.read_excel(file_path)
    elif ext == "json":
        df = pd.read_json(file_path)
    else:
        raise ValueError("Unsupported Format File")

# numerical statistics
    numerical_stats = {}
    for col in df.columns:
        if df[col].dtype in ["int","float"]:
          numerical_stats[col] = {
            "Count": int(df[col].count()),
            "Mean": round(df[col].mean()),
            "Std Dev": round(df[col].std()),
            "Min": round(df[col].min()),
            "Median": round(df[col].median()),
            "Max": round(df[col].max()),
            "Unique": int(df[col].nunique()),
        }
# categorical statistics
    categorical_stats = {}
    for col in df.columns:
        if df[col].dtype in ["object"]:
          categorical_stats[col] = {
            "Count": int(df[col].count()),
            "Unique Values": int(df[col].nunique()),
            "Most Common": df[col].mode().iloc[0] if not df[col].mode().empty else None,
            "Missing": int(df[col].isnull().sum()),
        }
# Data
    total_rows = len(df)
    total_cols = len(df.columns)
    duplicate_rows = df.duplicated().sum()
    total_cells = total_rows * total_cols
    missing_cells = df.isnull().sum().sum()
# cardinality
    cardinality ={} 
    for col in df.columns:
        cardinality[col] = (df[col].nunique() / total_cells) * 100

# result
    result = {
         "Data preview": {
            "preview":df.head(10).to_dict(orient="records"),
             "columns": df.columns.to_list()},
        "Statistics": {
            "numerical": numerical_stats,
            "categorical": categorical_stats
        },
        "Data Quality": {
            "Duplicate values": int(duplicate_rows),
            "Data Quality": ((total_cells - missing_cells)/ total_cells)*100,
            "Cardinality": cardinality
        }
        }
    return result
