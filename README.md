**Movie/TV Show Research Assistant (RAG Agent):**

***Overview:***
This project is a Retrieval Augmented Generation (RAG) Agent that helps users research movies and TV shows. It retrieves information from Wikipedia and YouTube to provide:

1)A brief summary of the movie/TV show.

2)A link to the official trailer on YouTube.

3)The application is built using Python and features a simple Tkinter-based GUI for user interaction.

***Features:***

1)Wikipedia Integration: Fetches a summary of the movie/TV show.

2)YouTube Integration: Searches for and provides a link to the official trailer.

3)User-Friendly GUI: Built with Tkinter for easy interaction.

4)Clickable Links: The YouTube trailer link is clickable and opens in the default web browser.

***Technologies Used:***

1)Python: Core programming language.

2)Wikipedia API: For fetching movie/TV show summaries.

3)YouTube Data API: For searching and retrieving trailer links.

4)Tkinter: For building the graphical user interface (GUI).
5)Google Cloud Platform: For accessing the YouTube Data API.

***Setup Instructions:***
1. Prerequisites

i)Python 3.8 or higher.

ii)A YouTube Data API key (free) from the Google Cloud Console.

2. Install Dependencies

Run the following command to install the required Python libraries:

pip install wikipedia-api google-api-python-client

3. Set Up the YouTube Data API Key

Replace the placeholder in the script with your YouTube Data API key:

YOUTUBE_API_KEY = "AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"  (Replace with your API key)

4. Run the Application

Clone the repository:

git clone "https://github.com/your-username/movie-research-assistant.git" (Replace with your repo url)

5)Navigate to the project directory:

cd rag_agent

6)Run the script:

python rag_agent.py

***How It Works:***

1)The user enters a movie or TV show name in the input field and clicks Search.

2)The application:

i)Fetches a summary of the movie/TV show from Wikipedia.

ii)Searches for the official trailer on YouTube using the YouTube Data API.

iii)Displays the results in the GUI.

iv)The YouTube trailer link is clickable, and clicking it opens the trailer in the default web browser.

***Challenges I faced:***

1)Wikipedia API User-Agent Requirement:

The Wikipedia API requires a user agent to identify the application. This was resolved by adding a custom user agent string during initialization.


2)YouTube Search with pytube:

The pytube library no longer supports the YouTube.search method. This was resolved by switching to the YouTube Data API.

3)GUI Development:

Ensuring the GUI was user-friendly and responsive required careful design and testing. The use of Tkinter made it easy to create a simple and functional interface.

4)Error Handling:

Handling cases where no results were found (e.g., invalid movie names) required robust error handling and user-friendly messages.

5)New APIs:

Working with new APIs was a hassle as im still learning about APIs and how they are integrated so working with the new ones was tough.I studied documentation and watched 
different Youtube videos to tackle that problem.
(https://www.mediawiki.org/wiki/API:Main_page) , (https://developers.google.com/youtube/v3/getting-started)

