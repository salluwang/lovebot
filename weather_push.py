import os
import requests

SENDKEY = os.getenv("SENDKEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

def get_weather(city="kaifeng", lang="en"):
    url = f"https://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&lang={lang}"
    response = requests.get(url)
    data = response.json()
    
    if "current" in data:
        weather = data["current"]["condition"]["text"]
        temp = data["current"]["temp_c"]
        feels_like = data["current"]["feelslike_c"]
        wind_speed = data["current"]["wind_kph"]
        wind_dir = data["current"]["wind_dir"]
        visibility = data["current"]["vis_km"]
        uv_index = data["current"]["uv"]
        rain_chance = data["current"]["precip_mm"]

        bike_suggestion = "Perfect for biking! 🚴✨"
        if wind_speed > 25:
            bike_suggestion = "⚠️ Strong winds today, ride with caution!"
        elif rain_chance > 0:
            bike_suggestion = "🌧️ Rain is expected, wear waterproof gear!"
        elif visibility < 3:
            bike_suggestion = "🌫️ Low visibility, be careful on the road!"
        elif uv_index > 7:
            bike_suggestion = "🌞 High UV index today, wear sunscreen!"

        return (
            f"**Weather in {city}: {weather}, {temp}°C**\n\n"
            f"🌡 **Feels like:** {feels_like}°C\n\n"
            f"💨 **Wind Speed:** {wind_speed} km/h ({wind_dir})\n\n"
            f"👀 **Visibility:** {visibility} km\n\n"
            f"🌞 **UV Index:** {uv_index}\n\n"
            f"🚴 {bike_suggestion}\n\n"
        )
    return "Weather information is unavailable."

def get_compliment():
    try:
        response = requests.get("https://complimentr.com/api")
        data = response.json()
        return data["compliment"].capitalize() + " 💖"
    except:
        return "Jasmine is the most most most beautiful in this world💕"

def send_wechat_message(language="en"):
    weather_info = get_weather(lang=language)
    compliment = get_compliment()

    title = "TREE HOLE🌳"
    message = (
        "💖 **Good morning, my love!** ☀️\n\n"
        "---\n"
        "**Here's today's biking weather update:**\n\n"
        f"{weather_info}\n\n"
        "---\n\n"
        "✨**Sally has something to say 🤓☝️**\n\n"
        f"{compliment}\n\n"
        "---\n\n"
        "**Diary📕**\n\n"
        "I love BANABN\n\n"
        "--2025.3.14 22:22\n\n"
    )

    url = f"https://sctapi.ftqq.com/{SENDKEY}.send"
    data = {
        "title": title,
        "desp": message
    }

    response = requests.post(url, data=data)
    print(response.json())

send_wechat_message(language="en")
