# Strava.cz Menu Scraper
This script fetches the daily menu from Strava.cz and converts it into a structured JSON format.
## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/kralicekgamer/strava.cz_menu_scraper
    cd strava.cz_menu_scraper
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Replace the placeholder URL in the `page.goto` method with the actual URL of the menu page in the `readJson.py` file.

2. Fetch the menu:
    ```python
    from readJson import read

    read()
    ```

3. Get and fetch today's menu:
    ```python
    from readJson import readToday

    readToday()
    ```

- Note: This script scrapes breakfast, lunch, and dinner. Remove any meal if it is not needed.

## License
This project is licensed under the MIT License.

