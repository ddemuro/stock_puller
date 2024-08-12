#!/usr/bin/python3
import sys
import requests
import subprocess
from datetime import datetime

CONTEXT = ""

# Run 'git diff' command and capture the output
# process = subprocess.Popen(["git", "diff"], stdout=subprocess.PIPE)
# output, error = process.communicate()

# Main function to run the script
def call_ai():
    
    # read the all the lines in the file ../results.csv
    CONTEXT = []
    CONTEXT.append("Given the following information in CSV format, return a change analysis of all tickers from the previous day to the next: ")
    with open('../results.csv') as f:
        lines = f.readlines()
        for line in lines:
            CONTEXT.append(line)

    # Generate a commit message prompt based on the filtered output
    msg = f"{CONTEXT}"

    # Define the API endpoint and payload
    key = "sk-----"
    url = "https://ai.takelan.com/ollama/api/generate"
    payload = {
            "model": "llama3.1:8b",
            "prompt": msg,
            "stream": False
    }
    headers = {"Authorization": f"Bearer {key}"}

    # Send a POST request to the API endpoint
    response = requests.post(url, json=payload, headers=headers)

    # Print the response from the API
    print(f"{response}\n")
