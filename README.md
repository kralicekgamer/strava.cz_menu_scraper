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
Run the script to fetch and process the menu:
```python
from readJson import read

data = read()
print(data)
```

## Function Reference

### `readJson.read()`
Fetches the menu from Strava.cz and returns it in JSON format.

**Returns:**
- `dict`: The menu data structured as JSON.

## License
This project is licensed under the MIT License.

