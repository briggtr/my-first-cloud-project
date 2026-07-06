import urllib.request
import re

# The target website to scrape
url = "https://example.com"

print(f"Fetching data from {url}...")

try:
    # Open the URL and read the HTML content
    with urllib.request.urlopen(url) as response:
        html = response.read().decode('utf-8')
    
    # Use Regex to find text between <h1> tags
    titles = re.findall(r'<h1>(.*?)</h1>', html)
    
    print("\n--- Found Headlines ---")
    for title in titles:
        print(f"• {title.strip()}")
        
except Exception as e:
    print(f"An error occurred: {e}")
