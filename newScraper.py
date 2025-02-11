import requests
import re
from bs4 import BeautifulSoup

def get_story_text(url):
    """
    Fetches the webpage at the given URL and extracts the plain text between
    <!-- CONTENT --> and <!-- VOTES --> markers.

    Parameters:
        url (str): The URL to scrape.

    Returns:
        str or None: The extracted plain text if successful; otherwise, None.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

    html = response.text

    # Capture content between <!-- CONTENT --> and <!-- VOTES -->
    pattern = re.compile(r'<!--\s*CONTENT\s*-->(.*?)<!--\s*VOTES\s*-->', re.DOTALL)
    match = pattern.search(html)
    if not match:
        print(f"Story markers not found in URL {url}")
        return None

    story_html = match.group(1)

    # Convert HTML to plain text using BeautifulSoup.
    soup = BeautifulSoup(story_html, 'html.parser')
    story_text = soup.get_text(separator="\n", strip=True)

    return story_text

def append_story_to_file(story_text, url, filename="stories.txt", delimiter="----"):
    """
    Appends the provided story text to a file along with the source URL and a delimiter.

    Parameters:
        story_text (str): The plain text to write to the file.
        url (str): The source URL (for reference).
        filename (str): The name of the file to which the story is appended.
        delimiter (str): The delimiter used to separate stories.
    """
    if not story_text:
        return

    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"URL: {url}\n")
            file.write(story_text + "\n")
            file.write(delimiter + "\n")
        print(f"Story from {url} appended successfully.")
    except Exception as e:
        print(f"Error writing story from {url} to file: {e}")

if __name__ == "__main__":
    print("Enter a URL to scrape (or type 'exit' to quit):")
    
    while True:
        url = input("URL: ").strip()
        if url.lower() == "exit":
            print("Exiting the scraper.")
            break
        if not url:
            print("No URL provided. Please try again.")
            continue
        
        story = get_story_text(url)
        if story:
            append_story_to_file(story, url)
        else:
            print("No story was extracted from this URL.")
