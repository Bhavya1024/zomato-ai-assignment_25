from bs4 import BeautifulSoup
import csv

# Load the HTML
with open('O_Pedra_pages/Menu.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

menu_data = []

# Go through each tab to extract section names and corresponding IDs
tabs = soup.select('ul.tabs-nav li a')
for tab in tabs:
    section_name = tab.get_text(strip=True)
    section_id = tab.get('href').lstrip('#')
    section = soup.find('section', id=section_id)
    
    if not section:
        print(f"⚠️ Couldn't find section: {section_id}")
        continue

    # Each menu subsection
    for menu_section in section.select('section.menu-section'):
        tag_name = menu_section.find('h2')
        tag = tag_name.get_text(strip=True) if tag_name else section_name

        # Each item in this menu subsection
        for item in menu_section.select('li.menu-item'):
            name_tag = item.select_one('p.menu-item__heading--name')
            desc_tag = item.select_one('p.menu-item__details--description')
            price_tag = item.select_one('p.menu-item__heading--price')  # optional, if exists

            item_name = name_tag.get_text(strip=True) if name_tag else ''
            description = desc_tag.get_text(strip=True) if desc_tag else ''
            price = price_tag.get_text(strip=True) if price_tag else ''

            if item_name:
                menu_data.append([section_name, tag, item_name, description, price])

# Save to CSV
with open('O_Pedra_Menu_Structured.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Section', 'Category', 'Item Name', 'Description', 'Price'])
    writer.writerows(menu_data)

print("✅ Extracted and saved menu data to 'O_Pedra_Menu_Structured.csv'")
