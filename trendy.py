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
    # first_topic = trending_container.find_all('div', class_='md-list-block first-list-item')
    # trending_topics = trending_container.find_all('div', class_='md-list-block')
    trending_topics = trending_container.find_all('div', class_='trending-item')

    # do just first
    beets = trending_topics[0].find('div', class_='details-top')
    tupac = beets.find('a').text
    print(f"1, {tupac}")

    # Extract the second and third trending topics
    # sndtrd = []
    # for topic in trending_topics[1:3] :
    #     deets = topic.find_all('div', class_='details-top')
    #     # Navigate through the nested elements to get the topic title
    #     topic_title = deets.find('a').text
    #     sndtrd.append(topic_title)

    for i, topic in enumerate(trending_topics[1:3], start=2) :
        deets = topic.find('div', class_='details-top')
        topi_titl = deets.find('a').text
        print(f"{i}, {topi_titl}")
else :
    print("trending topics container not found on the page.")

quit()