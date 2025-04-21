from bs4 import BeautifulSoup
import csv

# Load HTML content
with open('O_Pedra_pages/About Us.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Initialize dictionary
info = {
    'Name': 'O Pedro',
    'Address': '',
    'Phone': '',
    'Email': '',
    'Opening Hours': '',
    'What3Words': '',
    'Google Maps Link': '',
    'Latitude': '',
    'Longitude': ''
}

# Extract address
address_tag = soup.select_one('section#intro a[href^="https://maps.google.com"]')
if address_tag:
    info['Address'] = address_tag.get_text(strip=True)
    info['Google Maps Link'] = address_tag.get('href')

# Extract phone
phone_tag = soup.select_one('a[href^="tel:"]')
if phone_tag:
    info['Phone'] = phone_tag.get_text(strip=True)

# Extract email
email_tag = soup.select_one('a[href^="mailto:"]')
if email_tag:
    info['Email'] = email_tag.get_text(strip=True)

# Extract hours
hours_tag = soup.select_one('section#intro p:nth-of-type(2)')
if hours_tag:
    info['Opening Hours'] = hours_tag.get_text(strip=True)

# Extract What3Words
w3w_tag = soup.select_one('a[href^="https://w3w.co/"]')
if w3w_tag:
    info['What3Words'] = w3w_tag.get_text(strip=True)

# Extract latitude and longitude from map section
map_div = soup.select_one('div.gmaps')
if map_div:
    info['Latitude'] = map_div.get('data-gmaps-lat', '')
    info['Longitude'] = map_div.get('data-gmaps-lng', '')

# Save to CSV
with open('O_Pedra_Info.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=info.keys())
    writer.writeheader()
    writer.writerow(info)

print("📍 Extracted About Us information saved to 'O_Pedra_Info.csv'")
