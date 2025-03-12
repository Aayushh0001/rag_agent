import wikipediaapi
from googleapiclient.discovery import build
import tkinter as tk
from tkinter import scrolledtext
import webbrowser

wiki_wiki = wikipediaapi.Wikipedia(
    language='en',
    user_agent='MyMovieApp/1.0 (https://example.com; myemail@example.com)'
)

YOUTUBE_API_KEY = "AIzaSyARSYGt01LiRLgKpaiGBYZUHV_Eb52CZoo" 

def wikipedia_search(query):
    page = wiki_wiki.page(query)
    if page.exists():
        return page.summary
    else:
        return "No Wikipedia page found for this query."

def youtube_search(query, max_results=1):
    youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)
    request = youtube.search().list(
        q=query + " movie trailer",
        part='snippet',
        type='video',
        maxResults=max_results
    )
    response = request.execute()
    
    if response['items']:
        video_id = response['items'][0]['id']['videoId']
        return f"https://www.youtube.com/watch?v={video_id}"
    else:
        return None

def search_and_display(query):
    try:
        wiki_summary = wikipedia_search(query)
        if not wiki_summary:
            wiki_summary = "No Wikipedia summary found."
        
        youtube_link = youtube_search(query)
        if not youtube_link:
            youtube_link = "No YouTube trailer found."
        
        result_text = f"Query: {query}\n\n"
        result_text += f"Wikipedia Summary: {wiki_summary}\n\n"
        result_text += f"YouTube Trailer: {youtube_link}\n"
        
        return result_text
    except Exception as e:
        return f"An error occurred: {str(e)}"

def on_submit():
    query = entry.get()
    result = search_and_display(query)
    output_area.insert(tk.END, result + "\n\n")
    entry.delete(0, tk.END)

root = tk.Tk()
root.title("Movie/TV Show Research Assistant")

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

submit_button = tk.Button(root, text="Search", command=on_submit)
submit_button.pack(pady=10)

output_area = scrolledtext.ScrolledText(root, width=80, height=20)
output_area.pack(pady=10)

root.mainloop()