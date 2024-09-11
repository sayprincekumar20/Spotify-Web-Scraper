import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import csv

# Initialize the Chrome WebDriver
logging.basicConfig(filename='spotify_scraping.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s: %(message)s')
driver = webdriver.Chrome()
driver.maximize_window()

# Open Spotify login page
driver.get("https://open.spotify.com/collection/tracks")  #specify your track list
time.sleep(5)

# Log in to Spotify
button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='login-button']")
button.click()
time.sleep(10)

input_field = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="login-username"]')
input_field.send_keys("sayprincekumar20@gmail.com") # Enter you username
password_field = driver.find_element(By.CSS_SELECTOR, 'input[data-testid="login-password"]')
password_field.send_keys("P******5") # Enter your password
login_button = driver.find_element(By.CSS_SELECTOR, 'button[data-testid="login-button"]')
login_button.click()
time.sleep(10)

# Navigate to liked songs
try:
    div_element = driver.find_element(By.CSS_SELECTOR, 'div[role="button"][aria-disabled="false"][aria-labelledby^="listrow-title-spotify"][aria-describedby^="onClickHintspotify"]')
    div_element.click()
    time.sleep(10)
except Exception as e:
    # Log the error
    logging.error("Username or password is wrong.")
    driver.quit()
    exit()

# Open a CSV file in write mode
with open('tracklist.csv', 'w', newline='', encoding='utf-8') as csvfile:
    # Define the CSV writer
    writer = csv.writer(csvfile)
    # Write the header row
    writer.writerow(['Track Number', 'Song Name', 'Album Name', 'Artist Name', 'Duration'])

    # Set to store unique song names
    unique_songs = set()

    # Scroll and extract track information until reaching the end of the page
    i = 1
    while True:
        try:
            row = driver.find_element(By.XPATH, f"//div[@role='row'][@aria-rowindex='{i}']")
            driver.execute_script("arguments[0].scrollIntoView();", row)
            time.sleep(1)  # Adjust the wait time as necessary

            # Extract track information
            html_content = driver.page_source
            soup = BeautifulSoup(html_content, 'html.parser')
            tracklist = soup.find_all("div", class_="IjYxRc5luMiDPhKhZVUH")

            # Write the extracted data to the CSV file
            for track in tracklist:
                # Extract data from the track
                track_number = track.find("span", class_="xNyTkXEncSjszLNI65Nq").text.strip()
                song_name = track.find("div", class_="encore-text-body-medium").text.strip()
                s_name = ""
                for char in song_name:
                    if char == "(" or char == '-':
                        break
                    else:
                        s_name += char

                album_name = track.find("a", href=True, class_="standalone-ellipsis-one-line").text.strip()
                album_name = album_name.split('"')[-2] if '"' in album_name else album_name
                if not album_name:
                    album_name = s_name

                artist_name = track.find("span", class_="encore-text-body-small").text.strip()
                duration = track.find("div", class_="l5CmSxiQaap8rWOOpEpk").text.strip()

                # Check if the song name is already in the set
                if s_name not in unique_songs:
                    print("Track Number:", track_number)
                    print("Song Name:", s_name)
                    print("Album Name:", album_name)
                    print("Artist Name:", artist_name)
                    print("Duration:", duration)
                    print()

                    # Write the extracted data to the CSV file
                    writer.writerow([track_number, s_name, album_name, artist_name, duration])

                    # Add the song name to the set
                    unique_songs.add(s_name)
                    
            i += 10  # Move to the next row index
        except Exception as e:
            # Log the error
            logging.error("Error while scrolling and extracting data: %s", str(e))
            break  # Break the loop if an error occurs

# Wait for any pending operations and quit the driver
time.sleep(10)
driver.quit()