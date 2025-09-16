## Amir Daniali
## Code the Dream
## Week 10
## Task6 - OWASP


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import csv
from time import sleep
import pathlib

BASEDIR = pathlib.Path(__file__).parent
print("Basedir: ", BASEDIR)


def task6():
    """Task 6: Scraping Structured Data

    Goal:

    Extract a web page section and store the information.

        Use your browser developer tools to view this page: [https://owasp.org/www-project-top-ten/].  You are going to extract the top 10 security risks reported there.  Figure out how you will find them.

        Within your python_homework/assignment10 directory, write a script called owasp_top_10.py.  Use selenium to read this page.

        Find each of the top 10 vulnerabilities.  Hint: You will need XPath.  For each of the top 10 vulnerabilites, keep the vulnerability title and the href link in a dict.  Accumulate these dict objects in a list.

        Print out the list to make sure you have the right data.  Then, add code to the program to write it to a file called owasp_top_10.csv.  Verify that this file appears correct.

        Create a file, challenges.txt, also within your lesson9 directory.  In this file, describe any challenges you faced in completing this assignment and how you resolved them.
    """

    # Initialize the web driver

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Enable headless mode
    options.add_argument("--disable-gpu")  # Optional, recommended for Windows
    options.add_argument("--window-size=1920x1080")  # Optional, set window size

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    driver.get("https://owasp.org/www-project-top-ten/")
    sleep(3)

    elements = driver.find_elements(
        By.XPATH, "/html/body/main/div/div[1]/section[1]/ul[2]/li/a"
    )

    top_10 = []
    for element in elements:
        title = element.text.strip()
        href = element.get_attribute("href")
        top_10.append({"title": title, "link": href})

    for item in top_10:
        print(item)

    with open(BASEDIR / "owasp_top_10.csv", mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=["title", "link"])
        writer.writeheader()
        writer.writerows(top_10)

    driver.quit()


if __name__ == "__main__":
    task6()
