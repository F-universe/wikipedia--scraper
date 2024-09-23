from flask import Flask, request, render_template_string, session
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import logging
import time
import os

app = Flask(__name__)
app.secret_key = 'a_very_secure_secret_key'

logging.basicConfig(level=logging.DEBUG)

# Configure WebDriver
def create_driver():
    chromedriver_path = r'C:\Users\fabio\OneDrive\Desktop\webdriver\chromedriver.exe'

    options = Options()
    options.add_argument('--headless')  # Run in headless mode (no browser window)
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    service = ChromeService(executable_path=chromedriver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

# Function to use Selenium to get data from Wikipedia in English
def search_wikipedia(term):
    driver = create_driver()
    
    # Search on English Wikipedia
    search_url = f"https://en.wikipedia.org/wiki/{term.replace(' ', '_')}"
    driver.get(search_url)
    time.sleep(2)  # Wait for the page to load

    try:
        paragraphs = driver.find_elements(By.TAG_NAME, 'p')
        if paragraphs:
            content = ''
            for para in paragraphs:
                content += para.text + '\n'
        else:
            content = "No information found for this term."
    except Exception as e:
        content = f"Error extracting data: {e}"
    finally:
        driver.quit()
    
    return content.strip()

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    
    if request.method == 'POST':
        if 'download' in request.form:
            term = request.form['term']
            try:
                # Use Selenium to get the content of the Wikipedia page
                content = search_wikipedia(term)
                
                # Path to save the file
                save_directory = r'C:\Users\fabio\OneDrive\Desktop\wiki search1'
                if not os.path.exists(save_directory):
                    os.makedirs(save_directory)  # Create the directory if it doesn't exist
                
                file_path = os.path.join(save_directory, 'info.txt')
                
                # Save the content to a text file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                
                message = f'The data from the Wikipedia page was successfully downloaded to {file_path}.'
                session['downloaded'] = True
            except Exception as e:
                message = f"An error occurred: {e}"
    
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Wikipedia Scraper</title>
        <style>
            body { font-family: Arial, sans-serif; background-color: #f7f7f7; }
            form { max-width: 300px; margin: 50px auto; }
            input[type="text"], input[type="submit"] { width: 100%; padding: 10px; margin-bottom: 10px; border-radius: 5px; }
            input[type="submit"] { border: 1px solid #ddd; background-color: #5cb85c; color: white; }
        </style>
    </head>
    <body>
        <form method="POST">
            <input type="text" name="term" placeholder="Enter search term here">
            <input type="submit" name="download" value="Download Data">
        </form>
        {{ message }}
    </body>
    </html>
    ''', message=message)

if __name__ == '__main__':
    app.run(debug=True)
