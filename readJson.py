from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import json
import locale
from datetime import datetime


locale.setlocale(locale.LC_TIME, "czech") 

"""
This script reads the menu from the Strava.cz website and saves it to a JSON file.
"""
def read():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        # PASTE HERE YOUR LINK
        # example link: https://app.strava.cz/jidelnicky?jidelna=6218
        page.goto('https://app.strava.cz/jidelnicky?jidelna=6218')

        # Cookie accept
        try:
            page.click('button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll')
        except Exception as e:
            print("Nefungují sušenky:", e)

        page.wait_for_load_state('networkidle')

        content = page.content()

        browser.close()

    # Parse HTML
    soup = BeautifulSoup(content, 'html.parser')

    days_data = []

    # Find all days
    days = soup.find_all('div', class_='relative rounded-2xl border border-edge bg-surface-100 px-1.5 py-4 tablet:px-4 tablet:py-5 desktop:px-6')

    # Read data
    for day in days:
        day_data = {}

        date_element = day.find('h2')
        if date_element:
            date = date_element.text.strip()
            day_data["date"] = date
        else:
            day_data["date"] = "Datum nebylo nalezeno."

        breakfast_element = day.find('span', string='Snídaně')
        if breakfast_element:
            breakfast = breakfast_element.find_next('span', class_='InputLabel').text.strip()
            day_data["breakfast"] = breakfast
        else:
            day_data["breakfast"] = "Snídaně nebyla nalezena."

        lunch_section = day.find('span', string='Oběd')
        if lunch_section:
            lunch_items = lunch_section.find_next('div', class_='space-y-0.5').find_all('div', class_='flex w-full flex-col rounded-lg p-1')
            lunch_data = []
            for i, item in enumerate(lunch_items[:4]):
                lunch_label = item.find('span', class_='InputLabel')
                if lunch_label:
                    lunch_data.append(lunch_label.text.strip())
            day_data["lunch"] = lunch_data if lunch_data else "Oběd nebyl nalezen."
        else:
            day_data["lunch"] = "Oběd nebyl nalezen."

        dinner_element = day.find('span', string='Večeře')
        if dinner_element:
            dinner = dinner_element.find_next('span', class_='InputLabel').text.strip()
            day_data["dinner"] = dinner
        else:
            day_data["dinner"] = "Večeře nebyla nalezena."

        days_data.append(day_data)

    # Save to JSON
    with open('menuData.json', 'w', encoding='utf-8') as json_file:
        json.dump(days_data, json_file, ensure_ascii=False, indent=4)

"""
This function reads the menu from the JSON file and prints today's menu.
"""
def readToday():
    # Read JSON
    try: 
        with open('menuData.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

    # If file not found, run read() function
    except FileNotFoundError:
        read()
        with open('menuData.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

    # Get today's date
    today = datetime.today().strftime("%A %#d. %#m. %Y")  

    # Capitalize first letter of day
    today = today.capitalize()

    # Find today's menu
    today_menu = next((item for item in data if item["date"] == today), None)

    # Print today's menu
    if today_menu:
        # Today's menu exists but is not fetched from the web.
        if today_menu["breakfast"] == "Snídaně":
            read()

        print(json.dumps(today_menu, ensure_ascii=False, indent=4))

    else:
        print("No more food! Or prdele nefunguje to!")
        read()

    return today_menu
