import csv
from bs4 import BeautifulSoup

# Replace html_file_path and csv_file_path with the actual file paths on your computer
with open("bookmarks.html") as html_file, open("bookmarks.csv", "w", newline="") as csv_file:
    soup = BeautifulSoup(html_file, "html.parser")
    links = soup.find_all("a")
    writer = csv.writer(csv_file)
    for link in links:
        url = link.get("href")
        text = link.get_text()
        if url and "imgur.com" in url:
            writer.writerow([url, text])
