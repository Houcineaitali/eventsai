# Example Python script to fetch financial news from NewsAPI
import requests
import json

NEWS_API_KEY = "your_api_key"
url = f"https://newsapi.org/v2/everything?q=finance&apiKey={NEWS_API_KEY}"

response = requests.get(url)
data = response.json()

for article in data['articles']:
    title = article['title']
    summary = article['description']
    source = article['source']['name']
    # Process with AI (summarize, categorize)
    # Publish to your CMS
wp_url = "https://your-site.com/wp-json/wp/v2/posts"
wp_username = "admin"
wp_password = "password"  # Better to use an app password

headers = {
    'Content-Type': 'application/json',
}

data = {
    'title': 'Market News Update',
    'content': 'AI-generated summary here...',
    'status': 'publish'
}

response = requests.post(
    wp_url,
    headers=headers,
    json=data,
    auth=(wp_username, wp_password)
)
# Example Python script to fetch financial news from NewsAPI
import requests
import json

NEWS_API_KEY = "your_api_key"
url = f"https://newsapi.org/v2/everything?q=finance&apiKey={NEWS_API_KEY}"

response = requests.get(url)
data = response.json()

for article in data['articles']:
    title = article['title']
    summary = article['description']
    source = article['source']['name']
    # Process with AI (summarize, categorize)
    # Publish to your CMS