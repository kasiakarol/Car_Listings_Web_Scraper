# Car_Listings_Web_Scraper
A Python web scraper using BeautifulSoup for extracting car listing data from carpages.ca, including links, titles, prices, and colors, and saving the data in a CSV file.

**Description**
This Python script is designed to scrape car listing information from the website carpages.ca. It collects data about used cars, including their link, title, price, and color. The script is set to scrape the first five pages of the listings.

**Output**
The script outputs a CSV file named cars_scraper.csv, which includes the following columns:

- Link: The URL of the car listing.
- Title: The title of the listing.
- Price: The listed price of the car.
- Colour: The color of the car.

**Customization**
If you wish to change the output file path or the number of pages to scrape, modify the following lines in the script:

- output_file_path = 'cars_scraper.csv' - change this to your desired file path.
- max_page = 5 - change this to the desired number of pages to scrape.
