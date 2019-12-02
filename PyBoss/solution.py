import csv

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Create and open in write mode the file we will add the 
# new data  
with open('employee_clean.csv', 'w+') as file:
    # Write the new header once in the new file
    file.write("Emp ID,First Name,Last Name,DOB,SSN,State\n")
    # Now we open the old file to read and transform the data
    with open("employee_data.csv", "r") as in_file:
        # Transform the CSV line into a list
        data = csv.reader(in_file)
        # Skip the header
        header = next(data)    
        for row in data:
            id = row[0]
            first_name = row[1].split(" ")[0]
            last_name = row[1].split(" ")[1]
            ssn = "****-**-" + row[3][7:]
            date = row[2][5:7] +"/" + row[2][8:] + "/" + row[2][0:4] 
            state = us_state_abbrev.get(row[4])
            # Write the new data into the new file
            file.write(id + "," + first_name + "," + last_name + "," + ssn + "," + date + "," + state  + "\n")
