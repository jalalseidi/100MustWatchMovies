# Empire Online Best Movies Scraper

## Overview
This project is a Python web scraper that extracts the **top 100 movies** from Empire Online's archived "Best Movies" list. It retrieves movie titles, sorts them correctly, and saves them to a text file.

## Features
- Scrapes movie titles from **Empire Online's Best Movies** list.
- Correctly reverses the ranking so the #1 movie appears first.
- Saves the list to `movies.txt`.
- Handles potential request failures.

## Technologies Used
- **Python**
- **BeautifulSoup** (for web scraping)
- **Requests** (for fetching webpage content)

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/empire-movie-scraper.git
   cd empire-movie-scraper
   ```
2. Install dependencies:
   ```sh
   pip install beautifulsoup4 requests
   ```

## Usage
Run the script using:
```sh
python scraper.py
```

### Expected Output
The script creates a `movies.txt` file with movie titles in the correct order.
Example:
```
1. The Godfather
2. The Shawshank Redemption
3. Pulp Fiction
...
100. Some Movie
```

## Notes
- The scraper relies on the **Wayback Machine** snapshot, so future updates to the original site will not affect it.
- If the request fails, an error message is displayed.

## Contributing
Feel free to submit pull requests for improvements or additional features.

## License
This project is licensed under the MIT License.

