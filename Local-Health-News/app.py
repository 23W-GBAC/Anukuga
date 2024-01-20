from flask import Flask, render_template
from flask_frozen import Freezer
import requests
from datetime import datetime
import pytz
import asyncio
import httpx

app = Flask(__name__)
freezer = Freezer(app)

NEWS_API_KEY = 'e1891e03afba41dc8ee7ccd2d5cdb23c'

# Function to fetch IP address along with timezone and current time based on the IP
def fetch_ip_time_timezone():
    try:
        response = requests.get('https://ipinfo.io/json')
        response.raise_for_status()
        data = response.json()
        tz_str = data['timezone']
        ip_address = data['ip']

        # Create a datetime object for the current time in the detected time zone
        now = datetime.now(pytz.timezone(tz_str))
        return now, tz_str, ip_address
    except requests.RequestException as error:
        print('Error fetching timezone and time:', error)
        return None, None, None

# Function to format date as DD.MM.YYYY
def format_date(date):
    return date.strftime("%d.%m.%Y")

# Function to determine greeting based on time of day
def get_greeting(date):
    hour = date.hour
    if hour < 12:
        return 'Good Morning'
    elif hour < 18:
        return 'Good Afternoon'
    else:
        return 'Good Evening'

# Function for retrieving country info from IP
async def fetch_country_info_async():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get('https://ipinfo.io/json')
            response.raise_for_status()
            data = response.json()
            country_code = data['country'].lower()  # Country code
            region_name = data['region']
            return country_code, region_name
    except httpx.HTTPError as error:
        print('Error fetching country info:', error)
        return None, None

# Function for retrieving Health News based on the user's location
async def fetch_health_news_async(country_code):
    if not country_code:
        return 'No country code provided for fetching news'

    url = f'https://newsapi.org/v2/top-headlines?country={country_code}&category=health&apiKey={NEWS_API_KEY}'

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPError as error:
        print('Error fetching health news:', error)
        return None

# Function for formatting News Publish Date and Time
def format_news_date(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    return date_obj.strftime("%d.%m.%Y at %H:%M:%S")

def fetch_country_info():
    return asyncio.run(fetch_country_info_async())

def fetch_health_news(country_code):
    return asyncio.run(fetch_health_news_async(country_code))

# Function for retrieving country full name from country code
def get_country_name_from_api(country_code):
    url = f"https://restcountries.com/v2/alpha/{country_code}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['name']
    return None


@app.route('/')
def index():
    current_datetime, timezone_str, ip_address = fetch_ip_time_timezone()
    greeting, last_refreshed = "Unable to fetch time information.", None
    if current_datetime and timezone_str:
        greeting = get_greeting(current_datetime)
        formatted_date = format_date(current_datetime)
        last_refreshed = f"Last refreshed on {formatted_date} at {current_datetime.strftime('%H:%M:%S')} {timezone_str}"

    country_code, region_name = fetch_country_info()
    health_news = fetch_health_news(country_code)
    country_name = get_country_name_from_api(country_code)

    return render_template('index.html', greeting=greeting, last_refreshed=last_refreshed, health_news=health_news, format_news_date=format_news_date, country_name=country_name, region_name=region_name, ip_address=ip_address)

if __name__ == "__main__":
    freezer.freeze()
