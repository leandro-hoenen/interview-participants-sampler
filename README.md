# Participants Sample Generator

This Python script generates a random sample of participants from a list stored in a text file. The script reads the participants' data, generates a random sample, and stores the sample in a CSV file. It also creates a separate text file with the email addresses of the selected participants.

## Features

- User-friendly command-line interface
- Customizable sample size
- Error handling for invalid sample sizes
- Outputs a CSV file with the full list of participants
- Outputs a CSV file with the selected sample
- Outputs a text file with the email addresses of the selected sample

## Requirements

- Python 3.12

## Installation

1. Clone this repository to your local machine.
2. Navigate to the directory containing the script.

## Usage

1. Ensure that your participants data is in a file named `participants_raw.txt` in the `input` directory. if required, crawl the data from the following website: https://www.fhnw.ch/de/search_profiles#q=Dozent&faculty%5B%5D=1010&offset=180&limit=30The


2. Run the script with the command `python3 main.py`.
3. When prompted, enter the desired sample size. This must be a number between 1 and the total number of participants.
4. The script will create a `participants.csv` file in the `output` directory with the full list of participants, a `participants_sample.csv` file with the selected sample, and a `participants_sample_email.txt` file with the email addresses of the selected sample.