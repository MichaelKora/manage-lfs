import pandas as pd
  
# read CSV file
donations_results = pd.read_csv('Donnations.csv')
donors_results = pd.read_csv('Donors.csv')

donations_len = en(donations_len)
donors_len = len(donors_results)

print (f"Amount of entries in donations.csv is: {donations_len}")
print (f"Amount of entries in donors.csv is: {donors_len}")
