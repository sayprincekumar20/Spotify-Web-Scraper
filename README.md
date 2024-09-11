# Spotify Track Scraper
This project is a web scraping tool that extracts track information from Spotify using Selenium and BeautifulSoup. The script logs in to Spotify, navigates to the user's liked songs, and extracts track details into a CSV file.

## Features
* Logs into Spotify and navigates to the liked tracks page
* Extracts track details including Track Number, Song Name, Album Name, Artist Name, and Duration
* Saves the extracted data into a CSV file
* Uses Selenium for web automation and BeautifulSoup for parsing HTML
## Prerequisites
* Python 3.x: Ensure Python 3 is installed on your system.
* Google Chrome: The script uses the Chrome WebDriver. Make sure Google Chrome is installed.
* ChromeDriver: Download and install the appropriate version of ChromeDriver from ChromeDriver Downloads.
# Installation
 Clone the Repository

bash
 *     git clone https://github.com/sayprincelumar20/spotify-track-scraper.git
       cd spotify-track-scraper
## Install Required Python Packages

Create a virtual environment (optional but recommended):

bash
*     python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`
## Install the required packages using pip:

bash
*     pip install selenium beautifulsoup4
## Download ChromeDriver

Download the ChromeDriver version that matches your installed Chrome browser version from ChromeDriver Downloads and place it in a directory included in your system’s PATH.

## Configuration
1. Update Credentials

Open spotify_web_scraping.py and replace the placeholders with your Spotify credentials:

python

*     input_field.send_keys("Enter your email id")
*     password_field.send_keys("enter your password")
Note: Ensure that you handle your credentials securely and avoid hardcoding sensitive information in scripts.

2. Set the Path to ChromeDriver

Make sure ChromeDriver is accessible in your PATH or specify its path explicitly in the webdriver.Chrome() initialization.

## Usage
1. Run the Script
Execute the script from the command line:

*     python spotify_web_scraping.py
The script will log in to Spotify, navigate to your liked tracks, and save the track details into tracklist.csv.

2. Check the Output

* tracklist.csv: The CSV file where the extracted track information is stored.
* spotify_scraping.log: The log file that records any errors encountered during the scraping process.

## Contributing
Feel free to contribute to this project by submitting issues or pull requests. Ensure that your changes align with the project's goals and follow the coding standards.


## Contact
For any questions or issues, please contact sayprincekumar20@gmail.com.

