import pandas as pd
import sqlite3  # Built-in Python library for interacting with SQLite databases


def extract(file_path):
    # Load the dataset from the local file path
    df = pd.read_csv(file_path, delimiter=';')

    # Print out the first few rows and the column names
    print("DataFrame Columns:", df.columns.tolist())
    print("First few rows of the DataFrame:")  # Display the first few rows
    print(df.head())

    return df


def transform(df):
    # Clean the data by removing missing values and normalizing quality ratings
    df = df.dropna()  # Remove any rows that contain missing values => ensure data quality

    # Normalize the quality column
    df['quality'] = df['quality'].astype('category')

    return df


def load(df):
    # Load the transformed DataFrame into SQLite database
    conn = sqlite3.connect('wine_quality_data.db')  # Establish connection to SQLite database 'wine_quality_data.db'

    # If the database doesn't exist, it will be created
    df.to_sql('wine_quality', conn, if_exists='replace', index=False)  # Write DataFrame to SQL table 'wine_quality'
    conn.close()  # Close the database connection


if __name__ == "__main__":
    file_path = './winequality-red.csv'
    data = extract(file_path)
    transformed_data = transform(data)
    load(transformed_data)
