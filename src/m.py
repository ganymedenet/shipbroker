import json
import time

import requests
from bs4 import BeautifulSoup

# Replace with your Equasis login details
USERNAME = 'sergey.rossman@gmail.com'
PASSWORD = 'Derby777!'
HOME_URL = 'https://www.equasis.org/EquasisWeb/public/HomePage?fs=HomePage&P_ACTION=NEW_CONNECTION'
LOGIN_URL = 'https://www.equasis.org/EquasisWeb/authen/HomePage?fs=HomePage'

DATA_URL = 'https://www.equasis.org/EquasisWeb/restricted/ShipList?fs=ShipName'
SEARCH_URL = 'https://www.equasis.org/EquasisWeb/restricted/Search?fs=Search'

SHIP_INFO = 'https://www.equasis.org/EquasisWeb/restricted/ShipInfo?fs=Search'

# Start a session to persist cookies
session = requests.Session()

session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
    'Referer': 'https://www.equasis.org/EquasisWeb/public/HomePage?fs=HomePage&P_ACTION=NEW_CONNECTION',
    'Accept-Encoding': 'ggzip, deflate, br, zstd',
    'Content-Type': 'application/x-www-form-urlencoded'
})

# Get the login page
login_page = session.get(HOME_URL)

# Print the content of the login page for debugging


# Parse the login page
soup = BeautifulSoup(login_page.content, 'html.parser')

# Locate the correct login form (adjust if needed)
login_form = soup.find('form', {'name': 'formLogin'}) or soup.find('form', {'name': 'formLoginMobile'})

if login_form is None:
    print("Login form not found!")
else:
    # Extract necessary form data (e.g., hidden inputs)
    form_data = {}
    for input_tag in login_form.find_all('input'):
        if input_tag.get('name'):
            form_data[input_tag['name']] = input_tag.get('value')

    # Add username and password to the form data
    form_data['j_email'] = USERNAME
    form_data['j_password'] = PASSWORD

    # print(form_data)
    # Send the login request
    response = session.post(LOGIN_URL, data=form_data)

    # print(response.text)

    #
    #
    # # Check if login was successful
    # if 'Log Out' not in response.text:
    #     print("Login failed!")
    # else:
    #     print("Login successful!")

    imo_number = "9250543"

    # search_data = {
    #     'P_PAGE': '1',
    #     'P_PAGE_COMP': '1',
    #     'P_PAGE_SHIP': '1',
    #     'ongletActifSC': 'ship',
    #     'P_ENTREE_HOME_HIDDEN': imo_number,
    #     'P_ENTREE': imo_number,
    #     'checkbox-shipSearch': 'Ship',
    #     'Submit': 'Search'
    # }

    # time.sleep(1)

    # search_response = session.post(SEARCH_URL, data=search_data)
    #
    # # Parse the search results page

    #
    # print(search_soup)

    ship_search = {
        'P_IMO': imo_number,
    }
    ship_response = session.post(SHIP_INFO, data=ship_search)

    with open("./file.html", "w", encoding='utf-8') as file:
        file.write(ship_response.text)

    search_soup = BeautifulSoup(ship_response.content, 'html.parser')

    # print(search_soup)

    table = search_soup.find('table', class_='tableLS')

    # print(table)

    # Find all <tr> elements
    rows = table.find_all('tr')
    #
    # print(rows)
    #
    # # Loop through each row to find the 'Registered owner'

    result = dict()

    for row in rows:
        if 'Registered owner' in row.text:
            print("YES")
            columns = row.find_all('td')
            owner_name = columns[2].text.strip()  # Assuming owner name is in the third <td>
            owner_address = columns[3].text.strip()  # Assuming address is in the fourth <td>
            # print(f"Owner Name: {owner_name}")
            # print(f"Address: {owner_address}")
            # Exit the loop once the registered owner is found

            result = dict(
                owner_name=owner_name,
                owner_address=owner_address,

            )

            break

    print(json.dumps(result, indent=4))
