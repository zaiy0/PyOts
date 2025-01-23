from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service  
import time

PATH = "./chromedriver-win64/chromedriver.exe"
service = Service(PATH)

browser = webdriver.Chrome(service=service)

try:
    browser.get("https://www.youtube.com")

    time.sleep(2)

    search_box = browser.find_element(By.NAME, "search_query")

    search_query = "Rumah Modern"
    search_box.send_keys(search_query)

    search_box.send_keys(Keys.RETURN)

    time.sleep(3)

    results = browser.find_elements(By.CSS_SELECTOR, "ytd-video-renderer")

    video_links = []  
    for index, result in enumerate(results[:5], start=1):  
        title_element = result.find_element(By.CSS_SELECTOR, "h3 a")
        title = title_element.text
        link = title_element.get_attribute("href")
        video_links.append(link)
        print(f"{index}. {title} - {link}")

    choice = int(input("\nPilih nomor video yang ingin diputar (1-5): ")) - 1

    if 0 <= choice < len(video_links):
        browser.get(video_links[choice])
        print(f"Memutar video: {video_links[choice]}")
    else:
        print("Pilihan tidak valid.")

finally:
    input("Tekan Enter untuk menutup browser...") 
    browser.quit()
