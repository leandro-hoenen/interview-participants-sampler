import re
import random

# User (user-friendly) guide and input
welcome_message = """Welcome to the participants sample generator
This program reads the participants_raw.txt file and creates a participants sample stored in the /output folder.
"""

print(welcome_message)
sample_size = int(input("Enter the sample size: "))

# Define the output destination
output_destination = "output"

# Open the file in read mode and load the data
with open('input/participants_raw.txt', 'r') as file:
    data = file.read()

pattern = r"(?P<name>.+?)\nDozent.*?Fachhochschule Nordwestschweiz FHNW\nHochschule für Wirtschaft\n(?P<address>.+?)\nDirekt(?P<phone>.+?)\nE-Mail(?P<email>.+?)\n"
matches = re.finditer(pattern, data, re.DOTALL)

participants = []
for match in matches:
    participant = match.groupdict()
    participant['name'] = participant['name'].split("\n")[-1]
    participant['address'] = participant['address'].replace('\n', ', ')
    participants.append(participant)

# if sample size is less than 1 and greater than the number of participants, the program will exit
if sample_size < 1 or sample_size > len(participants):
    print(f"Sample size must be between 1 and {len(participants)}")
    exit()

# create a csv file if it does not exist and store the participants in it with the separator ";"
with open(f"{output_destination}/participants.csv", "w") as file:
    file.write("Name;Address;Phone;Email\n")
    for participant in participants:
        file.write(f"{participant['name']};{participant['address']};{participant['phone']};{participant['email']}\n")


# define a random sample of 30 participants from the list of participants
random_participants = random.sample(participants, sample_size)

# create a csv file if it does not exist and store the random participants in it with the separator ";"
with open(f"{output_destination}/participants_sample.csv", "w") as file:
    file.write("Name;Address;Phone;Email\n")
    for participant in random_participants:
        file.write(f"{participant['name']};{participant['address']};{participant['phone']};{participant['email']}\n")

with open(f"{output_destination}/participants_sample_email.txt", "w") as file:
    for participant in random_participants:
        file.write(f"{participant['email']}; ")

message = """The participants have been successfully stored in the file participants.csv
A sample of 30 participants has been selected and stored in the file participants_sample.css
The email addresses of the 30 randomly selected participants have been stored in the file participants_sample_email.txt
"""

print(message)
