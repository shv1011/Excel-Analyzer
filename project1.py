import pandas as pd

def load_excel(file_path):
    """Load the Excel file into a DataFrame."""
    try:
        df = pd.read_excel(file_path)
        print("Excel file loaded successfully!")
        return df
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

def count_occurrences(df, column, value):
    """Count occurrences of a value in a specified column."""
    try:
        # Normalize data: Strip spaces and convert to lowercase for comparison
        df[column] = df[column].astype(str).str.strip().str.lower()
        value = value.strip().lower()

        count = (df[column] == value).sum()
        print(f"The value '{value}' appears {count} times in the column '{column}'.")
    except Exception as e:
        print(f"Error counting occurrences: {e}")

def apply_filter(df, column, filter_value):
    """Apply a filter to the DataFrame and return the filtered data."""
    try:
        # Normalize data: Strip spaces and convert to lowercase for comparison
        df[column] = df[column].astype(str).str.strip().str.lower()
        filter_value = filter_value.strip().lower()

        filtered_data = df[df[column] == filter_value]
        print(f"Filtered Data (based on {column} == {filter_value}):\n")
        print(filtered_data)
        return filtered_data
    except Exception as e:
        print(f"Error applying filter: {e}")
        return None

def main():
    """Main function to run the program."""
    # Load the Excel file
    file_path = input("Enter the path to the Excel file: ")
    df = load_excel(file_path)
    
    if df is not None:
        print("\nColumns available in the file:", df.columns.tolist())

        # Count occurrences
        column_to_count = input("\nEnter the column name to count occurrences: ")
        value_to_count = input(f"Enter the value to count in column '{column_to_count}': ")
        count_occurrences(df, column_to_count, value_to_count)

        # Apply filter
        column_to_filter = input("\nEnter the column name to apply a filter: ")
        value_to_filter = input(f"Enter the value to filter in column '{column_to_filter}': ")
        filtered_data = apply_filter(df, column_to_filter, value_to_filter)

        # Save filtered data
        save_option = input("\nDo you want to save the filtered data? (yes/no): ").strip().lower()
        if save_option == "yes":
            output_file = input("Enter the output file name (with .xlsx extension): ")
            try:
                filtered_data.to_excel(output_file, index=False)
                print(f"Filtered data saved to {output_file}")
            except Exception as e:
                print(f"Error saving file: {e}")

if __name__ == "__main__":
    main()
