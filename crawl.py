import requests
from scrapy.selector import Selector

# Prepare url
city     = 'Binh-dinh'
main_url = 'https://www.airbnb.com.vn'
city_url = f'{main_url}/s/{city}/homes/'

# Create selector
html = requests.get(city_url).content
sel  = Selector(text=html)

# Get hotels
hotels = sel.css('div._1e9w8hic')
print('Number of hotels:', len(hotels))


# Find the next page url
next_page = sel.css('a._1bfat5l ::attr(href)').extract_first()
print('Next page:', '\n', next_page)


# Get main information
hotel = hotels[0]
title            = hotel.css('a ::attr(aria-label)').extract_first()
url_link         = hotel.css('::attr(href)').extract_first()
url_img          = hotel.css('img ::attr(src)').extract_first()
type_of_room     = hotel.css('div._b14dlit ::text').extract_first()

print("title: " ,title)
print("url_link: ",url_link)
print(url_img)
print(type_of_room)