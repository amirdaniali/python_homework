## Amir Daniali
## Code the Dream
## Week 10
## Web Scraping

from datetime import date
import pathlib
from typing import Dict, List
import pandas as pd
import json
from math import ceil
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

BASEDIR = pathlib.Path(__file__).parent
print("Basedir: ", BASEDIR)


def get_page_results(driver: webdriver) -> List[Dict]:
    """

        get_books.py. The program should import from selenium and webdriver_manager, as shown in your lesson.  You also need pandas and json.

        Add code to load the web page given in task 2.

        Find all the li elements in that page for the search list results.  You use the class values you stored in task 2 step 3.  Also use the tag name when you do the find, to make sure you get the right elements.

        Within your program, create an empty list called results.  You are going to add dict values to this list, one for each search result.

        Main loop: You iterate through the list of li entries.  For each, you find the entry that contains title of the book, and get the text for that entry.  Then you find the entries that contain the authors of the book, and get the text for each.  If you find more than one author, you want to join the author names with a semicolon ; between each.  Then you find the div that contains the format and the year, and then you find the span entry within it that contains this information.  You get that text too.  You now have three pieces of text.  Create a dict that stores these values, with the keys being Title, Author, and Format-Year.  Then append that dict to your results list.

        Create a DataFrame from this list of dicts.  Print the DataFrame.

    Hint You can put little print statements in at each step, to see if that part works.  For example, when you find all the li entries, you could print out the length of the list.  Then, you could just implement the part of the main loop that finds the Title, and just print out that title.  In this way, you can get the program done incrementally.

    For Further Thought  You are getting the search results from the first page of the search results list.  How would you get all the search results from all the pages?  How can you make the program do this regardless of how many pages you might have?  Optional: Change your program to page through the search results so as to get all of the results.  However! You need to make sure your program pauses between pages.  Fast screen scraping, where many requests are sent in short order, is an abuse of the privilege.
    """

    # Initialize list
    results: List[Dict] = []

    body = driver.find_element(By.CSS_SELECTOR, "body")
    if body:
        search_elements = body.find_elements(
            By.CSS_SELECTOR, "li.row"
        )  # the search result elements
        for element in search_elements:

            element_dict = {}

            title = element.find_elements(By.CSS_SELECTOR, ".title-content")
            if len(title) > 0:
                # print("title: ", title[0].text)
                element_dict["Title"] = title[0].text
            else:
                element_dict["Title"] = "Unknown"

            authors = element.find_elements(By.CSS_SELECTOR, ".author-link")
            authors_list: List[str] = []
            if len(authors) > 0:
                for author in authors:
                    # print("author: ", author.text)
                    authors_list.append(author.text)
                element_dict["Author"] = ";".join(authors_list)
            else:
                element_dict["Author"] = "Unknown"

            format = element.find_elements(By.CSS_SELECTOR, ".display-info-primary")
            if len(format) > 0:
                # print("format-year: ", format[0].text)
                element_dict["Format-Year"] = format[0].text
            else:
                element_dict["Format-Year"] = "Unknown"

            results.append(element_dict)

    return results


def get_all_search_results(base_url) -> List[Dict]:

    # Initialize the web driver

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Enable headless mode
    options.add_argument("--disable-gpu")  # Optional, recommended for Windows
    options.add_argument("--window-size=1920x1080")  # Optional, set window size

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    driver.get(base_url)

    body = driver.find_element(By.CSS_SELECTOR, "body")
    if body:
        pagination = body.find_elements(By.CSS_SELECTOR, ".cp-pagination-label")
        if len(pagination) > 0:
            pagination_text = pagination[0].text
            # Str Format: 1 to 20 of 269 results

            pagination_info = pagination_text.split()
            # Format:  ['1', 'to', '20', 'of', '269', 'results']

            page_length = 1 + int(pagination_info[2]) - int(pagination_info[0])
            total = int(pagination_info[4])

            number_of_steps = ceil(total / page_length)

    all_results: List[Dict] = []

    for page_number in range(1, number_of_steps + 1):
        print(
            f"Processing Page {page_number} and Result Items {(page_number-1)*page_length + 1} to {page_number*page_length}",
            end="\r",
        )
        driver.get(base_url + f"&page={page_number}")
        page_results = get_page_results(driver)
        all_results.extend(page_results)

        sleep(2)

        print(
            f"Finished Processing Page: {page_number}                                  "
        )

    driver.close()
    return all_results


if __name__ == "__main__":
    search_url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"

    results = get_all_search_results(search_url)
    df = pd.DataFrame(results)

    print("\nSearch Results\n")
    print(df.head(20))

    print("\nAll Results have been processed.")

    task4_details = """Modify your program to do the following:
    Write the DataFrame to a file called get_books.csv, within the assignment10 folder.  Examine the file to see if it looks right.
    Write the results list out to a file called get_books.json, also within the assignment10 folder.  You should write it out in JSON format.  Examine the file to see if it looks right.
    """

    df.to_csv(BASEDIR / "get_books.csv")
    with open(BASEDIR / "get_books.json", "w") as file:
        json.dump(results, file, indent=4)

    print("Finished Writing to disk.")
