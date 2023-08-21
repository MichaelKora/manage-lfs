import csv, sys
  
# read CSV file
with open('.git/lfs/objects/Donations.csv', newline='') as f1:
    donnations_reader = csv.reader(f1)
    donations_len = sum(1 for row in donnations_reader)  # fileObject is your csv.reader
    
with open('.git/lfs/objects/Donors.csv', newline='') as f2:
    donors_reader = csv.reader(f2)
    donors_len = sum(1 for row in donors_reader)  # fileObject is your csv.reader

# donations_results = pd.read_csv('')
# donors_results = pd.read_csv('Donors.csv')

# donations_len = en(donations_len)
# donors_len = len(donors_results)

print (f"Amount of entries in donations.csv is: {donations_len}")
print (f"Amount of entries in donors.csv is: {donors_len}")
