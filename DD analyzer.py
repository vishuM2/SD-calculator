import pandas as pd

def demographic_data_analyzer(file_path):
    # Load the data into a Pandas DataFrame
    df = pd.read_csv(file_path)

    # Display the first few rows of the DataFrame
    print("Sample of the data:")
    print(df.head())

    # Basic statistics
    print("\nBasic statistics:")
    print(df.describe())

    # Gender distribution
    print("\nGender distribution:")
    print(df['gender'].value_counts())

    # Age statistics
    print("\nAge statistics:")
    print("Mean age:", df['age'].mean())
    print("Median age:", df['age'].median())
    print("Oldest person:", df['age'].max())
    print("Youngest person:", df['age'].min())

    # Ethnicity distribution
    print("\nEthnicity distribution:")
    print(df['ethnicity'].value_counts())

    # Education level distribution
    print("\nEducation level distribution:")
    print(df['education_level'].value_counts())

    # Employment status distribution
    print("\nEmployment status distribution:")
    print(df['employment_status'].value_counts())

if __name__ == "__main__":
    # Provide the path to your demographic data CSV file
    file_path = "path/to/your/demographic_data.csv"
    demographic_data_analyzer(file_path)
