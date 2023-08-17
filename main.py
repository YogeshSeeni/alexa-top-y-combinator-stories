import requests

def get_top_stories():
    res = [] #Stores top 10 stories title, type, source url, and id

    #Get Y-Combinator IDs for top 10 stories
    stories = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty").json()[:10] 

    for story_id in stories:
        story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty").json()
        
        res.append({"title": story["title"], "type": story["type"], "url": story["url"], "id": story["id"]})

    return res

def web_scraper():
    pass

def text_summarization():
    pass