Code Description - Wikipedia Scraper
This project is a web application built with Flask and Selenium that allows users to extract content from a Wikipedia page based on a search term they input. The user can enter a search term, and the application fetches data from the corresponding Wikipedia page in English and saves it to a text file on the computer.

Project Structure
WebDriver Setup: The function create_driver sets up and launches the Chrome WebDriver using Selenium. The driver runs in headless mode, meaning that the browsing occurs without opening a visible browser window. This makes the application more lightweight and efficient. The path to the ChromeDriver is specified, and execution is optimized by disabling the GPU and sandbox.

Wikipedia Search: The function search_wikipedia is the core of the scraping logic. Given a search term entered by the user, this function builds a URL to search for the corresponding page on English Wikipedia. After loading the page, the function uses Selenium to extract all text found in paragraph tags. If the page contains no paragraphs or an error occurs, an appropriate message is returned. In the end, the WebDriver is closed to free up resources.

Flask Application: The application uses Flask to provide a web interface to the user. When the user visits the main page ("/"), they are presented with a form where they can enter a search term. After entering the term and submitting the form, Flask handles the POST request. At this point, the scraping function (search_wikipedia) is invoked, and the Wikipedia content is saved to a text file.

File Handling: The content extracted from Wikipedia is saved locally in the directory C:\Users\fabio\OneDrive\Desktop\wiki search1. If the directory does not exist, it is automatically created. The file in which the extracted text is saved is named info.txt. The user is informed of the file path where the data was saved through a message displayed on the web page.

Web Interface: The web interface is very simple and user-friendly. It includes an HTML form with a text field where the user can enter a search term and a button to submit the form. After the data is submitted, the user receives a message confirming whether the data was successfully downloaded or if an error occurred.

Error Handling: If an error occurs (e.g., if Wikipedia is not accessible or the searched page doesn’t exist), an error message is displayed both in the output file and on the web interface. This keeps the user informed of any issues.

Final Thoughts
The application is designed to be simple and fast, with a minimal interface that allows the user to search Wikipedia and quickly retrieve results.
The use of headless Selenium ensures that the scraping process runs without disturbing the user with visible browser windows.
The code is easily extendable and can be adapted to include additional features like the ability to select the Wikipedia language or save results in different formats (such as PDF or CSV).
