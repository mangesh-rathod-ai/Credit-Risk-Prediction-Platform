import pandas as pd
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Dataset paths
TRAIN_PATH = PROJECT_ROOT / "data" / "application_train.csv"
TEST_PATH = PROJECT_ROOT / "data" / "application_test.csv"


def load_train_data():
    """Load training dataset."""
    df = pd.read_csv(TRAIN_PATH)
    return df


def load_test_data():
    """Load test dataset."""
    df = pd.read_csv(TEST_PATH)
    return df


if __name__ == "__main__":

    train_df = load_train_data()
    test_df = load_test_data()

    print("=" * 60)
    print("Training Dataset")
    print("=" * 60)
    print(train_df.shape)

    print("\nFirst 5 rows")
    print(train_df.head())

    print("\nInformation")
    print(train_df.info())

    print("\nMissing Values")
    print(train_df.isnull().sum().head(20))

    print("\nTarget Distribution")
    print(train_df["TARGET"].value_counts())