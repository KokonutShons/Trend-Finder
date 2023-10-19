import requests
from bs4 import BeautifulSoup

# Send an HTTP GET request to Google Trends
url = 'https://trends.google.com/trends/trendingsearches/daily'
response = requests.get(url)

# Parse the HTML Content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the container that holds the trending topics
trending_container = soup.find('div', class_='feed-list-wrapper')

if trending_container :
    # Find all trending topics within the container
    first_topic = trending_container.find_all('div', class_='md-list-block first-list-item')
    trending_topics = trending_container.find_all('div', class_='md-list-block')

    # do just first
    beets = first_topic.find_all('div', class_='details-top')
    tupac = beets.find('a').text
    print(tupac)

    # Extract the second and third trending topics
    sndtrd = []
    for topic in trending_topics[1:3] :
        deets = topic.find_all('div', class_='details-top')
        # Navigate through the nested elements to get the topic title
        topic_title = deets.find('a').text
        sndtrd.append(topic_title)

    for i, topic in enumerate(sndtrd, start=1) :
        print(f"{i}, {topic}")
else :
    print("trending topics container not found on the page.")

quit()