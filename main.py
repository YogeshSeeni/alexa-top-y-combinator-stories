import requests
import bs4

def get_top_stories():
    res = [] #Stores top 10 stories title, type, source url, and id

    #Get Y-Combinator IDs for top 10 stories
    stories = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty").json()[:10] 

    for story_id in stories:
        story = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty").json()
        
        res.append({"title": story["title"], "type": story["type"], "url": story["url"], "id": story["id"]})

    return res

def web_scraper(stories):
    full_texts = {} #Stores title and all text from source url

    for story in stories:
        #Get Full Text from Story URL
        res = requests.get(story["url"])
        soup = bs4.BeautifulSoup(res.text)
        full_text = soup.body.get_text(" ", strip=True)

        #Create Key-Value Pair between title of Story and Full Text
        full_texts[story["title"]] = full_text

    return full_texts


def text_summarization():
    pass

top_stories = get_top_stories()
scraped_texts = web_scraper(top_stories)

for k, v in scraped_texts.items():
    print(k, v)
    break