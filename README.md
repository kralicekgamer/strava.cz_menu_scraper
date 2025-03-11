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
- Replace the placeholder URL in the `page.goto` method with the actual URL of the menu page. (line 16)

Run the script to fetch and process the menu:
```python
from readJson import read

data = read()
print(data)
```

## License
This project is licensed under the MIT License.

