#Hi this I´m David Flores and this is my proyect for PyPol :)
import csv
import os

# Get the absolute path to the CSV file
file_path = os.path.abspath('PyPoll/Resources/election_data.csv')
output_directory = "PyPoll/Analysis"
output_file = "Votes_analysis.txt"
full_file_path = os.path.join(output_directory, output_file)

Total_Votes = 0
Votes_for_Charles_Casper_Stockham = 0
Votes_for_Diana_DeGette = 0
Votes_for_Raymon_Anthony = 0


with open(file_path) as votes_data:
    votes_data_read = csv.reader(votes_data, delimiter=',')
    titles = next(votes_data_read)
    
    for rows in votes_data_read:
        Total_Votes +=1
        
        if rows[2] == 'Charles Casper Stockham':
            Votes_for_Charles_Casper_Stockham += 1
        elif rows[2] == 'Diana DeGette':
            Votes_for_Diana_DeGette += 1
        elif rows[2] == 'Raymon Anthony Doane':
            Votes_for_Raymon_Anthony += 1   
        
# Calcular porcentajes
Charles_percent = (Votes_for_Charles_Casper_Stockham / Total_Votes) * 100
Diana_percent = (Votes_for_Diana_DeGette / Total_Votes) * 100
Raymon_percent = (Votes_for_Raymon_Anthony / Total_Votes) * 100

# Determinar el ganador
if Votes_for_Charles_Casper_Stockham > Votes_for_Diana_DeGette and Votes_for_Charles_Casper_Stockham > Votes_for_Raymon_Anthony:
    Winner = 'Charles Casper Stockham'
elif Votes_for_Diana_DeGette > Votes_for_Charles_Casper_Stockham and Votes_for_Diana_DeGette > Votes_for_Raymon_Anthony:
    Winner = 'Diana DeGette'
else:
    Winner = 'Raymon Anthony Doane'         
            
            
            
            
Votes_analysis = (
    f'Election Results\n'
    f'----------------------------\n'
    f'Total Votes: {Total_Votes}\n'
    f'-------------------------\n'
    f'Charles Casper Stockham: {Charles_percent:.3f}% ({Votes_for_Charles_Casper_Stockham})\n'
    f'Diana DeGette: {Diana_percent:.3f}% ({Votes_for_Diana_DeGette})\n'
    f'Raymon Anthony Doane: {Raymon_percent:.3f}% ({Votes_for_Raymon_Anthony})\n'
    f'----------------------------\n'
    f'Winner: {Winner}\n'
    f'----------------------------\n'

)

print(Votes_analysis)

output_file = "Votes_analysis.txt"
with open(full_file_path, "w") as txt_file:
    txt_file.write(Votes_analysis)