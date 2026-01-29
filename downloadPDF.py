from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

download_dir = "targetDirectory"


def launch_chrome_browser():
    """
    Launches the Chrome browser, navigates to a URL, and quits.
    """
    try:

        options = Options()
        options.add_experimental_option('prefs', {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True
        }
                                        )

        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        print("Chrome browser launched successfully.")

        # Navigate to a website
        driver.get("URL")
        print(f"Navigated to: {driver.title}")
        #//*[@id="mainContentWrapper"]/div/div[2]/div/table
        #//*[@id="mainContentWrapper"]/div/table/tbody/tr[5]/td[1]/a
        #//*[@id="mainContentWrapper"]/div/div[2]/div/table[2]/tbody/tr[3]/td[1]

        for n in range(1,33):
            print("here")
            i = str(n)
            rows = driver.find_elements(By.XPATH, "//*[@id='mainContentWrapper']/div/div[2]/div/table[2]/tbody/tr[" + i + "]")
            for row in rows:
                    cols = row.find_elements(By.TAG_NAME, "td")
                    print(len(cols))
                    print(cols[0].text)
                    try:
                        a_tag_lesson = cols[0].find_element(By.TAG_NAME, "a")
                        #a_tag_brief = cols[7].find_element(By.TAG_NAME, "a")
                        a_tag_worksheet = cols[8].find_element(By.TAG_NAME, "a")
                        lesson_name = a_tag_lesson.get_attribute("href")
                        #brief = a_tag_brief.get_attribute("href")
                        worksheet = a_tag_worksheet.get_attribute("href")
                        print(f"The href value is: {lesson_name}")
                        driver.get(lesson_name)
                        time.sleep(30)
                        #driver.get(brief)
                        time.sleep(30)
                        driver.get(worksheet)
                        time.sleep(30)

                    except NoSuchElementException:
                                print("no link - in exception")
                                pass


                    
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser session
        if 'driver' in locals() and driver is not None:
            driver.quit()
            print("Browser closed.")

if __name__ == "__main__":
    launch_chrome_browser()

