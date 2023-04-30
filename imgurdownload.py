import csv
import os
import requests
import time

# Replace CLIENT_ID with your actual Client ID
headers = {"Authorization": "Client-ID CLIENT_ID"}

# Create a "downloads" directory if it doesn't exist
if not os.path.exists("downloads"):
    os.makedirs("downloads")

# Replace csv_file_path with the path to your CSV file
with open("bookmarks.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        imgur_url = row[0]
        response = requests.get(imgur_url, headers=headers)
        try:
            if response.status_code >= 400:
                # Log the name of the file for 4XX errors
                print(f"Error: {row[1]} ({imgur_url}) returned status code {response.status_code}.")
            else:
                # Get the file name from the second column of the CSV file
                file_name = f"{row[1]}.jpg"
                # Save the image to the "downloads" directory
                file_path = os.path.join("downloads", file_name)
                with open(file_path, "wb") as f:
                    f.write(response.content)
                print(f"Downloaded {row[1]} ({imgur_url}) with response code {response.status_code}.")
                time.sleep(1) # Add a 1 second delay
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1) # Add a 1 second delay
