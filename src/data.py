# src/data.py

import pandas as pd
import numpy as np

def load_raw(path: str) -> pd.DataFrame:
    """
    Load CSV .
    """
    return pd.read_csv(path)

def clean_missing(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values:
      
    """
    df = df.copy()
    # flags
    df['contact_missing']  = df['contact'].isna().astype(int)
    df['poutcome_missing'] = df['poutcome'].isna().astype(int)
    # fill
    df['contact']  = df['contact'].fillna('unknown')
    df['poutcome'] = df['poutcome'].fillna('unknown')
    df['pdays']    = df['pdays'].fillna(-1).astype(int)
    return df

def map_binaries(df: pd.DataFrame, cols=None) -> pd.DataFrame:
    """
    Map column
    """
    df = df.copy()
    if cols is None:
        cols = ['default','housing','loan','y']
    for c in cols:
        df[c] = df[c].map({'yes':1,'no':0}).astype(int)
    return df

def save_processed(df: pd.DataFrame, path: str) -> None:
    """
    processed DF to CSV.
    """
    df.to_csv(path, index=False)

def get_data(raw_path: str, processed_path: str) -> pd.DataFrame:
    """
    Load, apply and map, save & return.
    """
    df = load_raw(raw_path)
    df = clean_missing(df)
    df = map_binaries(df)
    save_processed(df, processed_path)
    return df
