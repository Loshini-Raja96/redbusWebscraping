import pandas as pd
import glob

def export_csv_file(input):
   # Path to the folder containing CSV files
   file_paths = glob.glob(f"{input}/*.csv")

   # Read each files into dataframe and store it in a list
   df = [pd.read_csv(file) for file in file_paths]

   # concatenate all dataframes in the list 
   combined_df=pd.concat(df,ignore_index=True)
   
   return combined_df

combined_df=export_csv_file('exportedCsvFiles')
combined_df.to_csv("bus_routes.csv", index=False)


