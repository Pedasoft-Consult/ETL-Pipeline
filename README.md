# Wine Quality Data Pipeline

This project implements a simple Extract-Transform-Load (ETL) pipeline for processing wine quality data. The pipeline reads data from a CSV file, cleans and transforms the data, and then loads it into an SQLite database for further analysis.

## Table of Contents
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [License](#license)

## Overview
The ETL pipeline performs the following steps:
1. **Extract**: Reads the wine quality dataset from a CSV file.
2. **Transform**: Cleans the dataset by removing missing values and normalizes the quality ratings.
3. **Load**: Saves the cleaned and transformed dataset into an SQLite database.

## Prerequisites
Ensure you have the following installed on your system:
- Python 3.7 or later
- SQLite (comes pre-installed with Python)
- Required Python packages: `pandas`

## Installation
1. Clone the repository or download the script.
   ```bash
   git clone https://github.com/your-repo/wine-quality-etl.git
   cd wine-quality-etl
   ```
2. Install the required Python packages using `pip`:
   ```bash
   pip install pandas
   ```

## Usage
1. Place your wine quality dataset (`winequality-red.csv`) in the same directory as the script.
2. Run the script:
   ```bash
   python etl_pipeline.py
   ```
3. The processed data will be saved in an SQLite database named `wine_quality_data.db` in the same directory.

### Input
The input file should be a CSV file with the delimiter `;`. For example:
```
fixed_acidity;volatile_acidity;citric_acid;residual_sugar;chlorides;free_sulfur_dioxide;total_sulfur_dioxide;density;pH;sulphates;alcohol;quality
7.4;0.7;0;1.9;0.076;11;34;0.9978;3.51;0.56;9.4;5
...
```

### Output
The transformed data is saved into an SQLite database table `wine_quality`. Each column in the CSV file corresponds to a column in the database table.

## Code Structure
- `etl_pipeline.py`: Contains the ETL logic, including the `extract`, `transform`, and `load` functions.

### Functions
#### `extract(file_path)`
- **Input**: Path to the CSV file.
- **Output**: A pandas DataFrame containing the raw data.
- **Description**: Loads the dataset and prints the first few rows and column names for verification.

#### `transform(df)`
- **Input**: A pandas DataFrame with raw data.
- **Output**: A pandas DataFrame with cleaned and normalized data.
- **Description**: Cleans the data by removing rows with missing values and normalizes the `quality` column.

#### `load(df)`
- **Input**: A pandas DataFrame with cleaned data.
- **Output**: None.
- **Description**: Saves the transformed data into an SQLite database table named `wine_quality`.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

