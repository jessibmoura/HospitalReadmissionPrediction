from ucimlrepo import fetch_ucirepo
import json

def main():
    # fetch dataset 
    diabetes_130_us_hospitals_for_years_1999_2008 = fetch_ucirepo(id=296)

    # data (as pandas dataframes) 
    X = diabetes_130_us_hospitals_for_years_1999_2008.data.features 
    y = diabetes_130_us_hospitals_for_years_1999_2008.data.targets
    dataset = diabetes_130_us_hospitals_for_years_1999_2008.data.original
    
    # metadata 
    print(diabetes_130_us_hospitals_for_years_1999_2008.metadata)
    metadata = diabetes_130_us_hospitals_for_years_1999_2008.metadata
    
    # variable information
    print(diabetes_130_us_hospitals_for_years_1999_2008.variables)
    variable_info = diabetes_130_us_hospitals_for_years_1999_2008.variables

    return dataset, metadata, variable_info

if __name__ == "__main__":
    dataset, metadata, variable_info = main()

    dataset.to_csv("data/raw/dataset.csv", index=False)

    with open("data/raw/metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)
    
    variable_info.to_csv("data/raw/variable_info.csv", index=False)