# Trustpilot Review Scraper

## Description

This project is a web scraper designed to extract reviews and trust scores for various businesses listed on Trustpilot. The scraper collects data from multiple categories, including:

- Hotels
- Financial Institutions
- Bars and Cafes
- Doctors and Surgeons
- Movies and Music

The data is collected from multiple pages within each category and is compiled into an Excel file.

## Features

- Scrapes businesses' names, trust scores, total reviews, and locations.
- Retrieves detailed reviews from the individual business pages.
- Outputs the collected data into an Excel file.

## Installation

To run the scraper, you need to have Python installed along with the necessary libraries. Install the required packages using pip:

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

## Usage

1. **Run the Python script**:
   ```bash
   HOTELS.py
   
## Script Functionality

- The script fetches HTML content from multiple pages of Trustpilot categories.
- It uses BeautifulSoup to parse the HTML and extract relevant information:
  - **NAME**: The name of the business.
  - **TRUST SCORE**: The trust score of the business.
  - **TOTAL REVIEWS**: The number of reviews for the business.
  - **URL**: The URL to the business's Trustpilot page.
  - **LOCATION**: The location of the business.
- The data is compiled into a pandas DataFrame.
- The DataFrame is cleaned and reformatted as needed.
- Finally, the DataFrame is saved into an Excel file named `HOTELS.xlsx`.

## Languages and Technologies

This project involves scraping reviews related to the following categories and technologies:

- **Python**: The programming language used to write the scraper.
- **Requests**: A Python library for making HTTP requests.
- **BeautifulSoup4**: A library used for parsing HTML and XML documents.
- **Pandas**: A data manipulation library for Python used to handle data and export it to Excel.
- **Excel**: The format used to save the scraped data.

## Built With

- Python
- BeautifulSoup4 - For web scraping
- Requests - For handling HTTP requests
- Pandas - For data manipulation and exporting to Excel

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to fork the repository and submit a pull request.


## Acknowledgments

- Thanks to the open-source community for the tools and libraries used in this project.
- Inspired by the need to analyze reviews across different categories on Trustpilot.
