import pytest
import pandas as pd

@pytest.fixture
def source_df():
    return pd.read_csv("data/customer_transactions_source.csv")

@pytest.fixture
def target_df():
    return pd.read_csv("data/customer_transactions_target.csv")

def test_validate_columns(source_df, target_df):
    expected_columns = list(source_df.columns)
    actual_columns = list(target_df.columns)
    assert expected_columns == actual_columns, "Column mismatch between source and target"

def test_validate_data_types(source_df, target_df):
    for col in source_df.columns:
        assert source_df[col].dtype == target_df[col].dtype, f"Data type mismatch in column {col}"
        
def test_amount_positive(target_df):
    assert (target_df["amount"] >= 0).all(), "Negative amounts found"
    
def test_no_duplicate_rows(target_df):
    duplicate_count = target_df.duplicated().sum()
    assert duplicate_count == 0, f"Duplicate rows found: {duplicate_count}"

def test_no_empty_values(target_df):
    # Check for NaN or empty strings across the whole DataFrame
    empty_count = target_df.isnull().sum().sum() + (target_df.eq("").sum().sum())
    assert empty_count == 0, f"Empty values found: {empty_count}"

def test_transaction_type_valid(target_df):
    valid_types = {"credit", "debit"}
    invalid_types = target_df[~target_df["transaction_type"].isin(valid_types)]
    assert invalid_types.empty, f"Wrong transaction types found: {invalid_types['transaction_type'].unique()}"
