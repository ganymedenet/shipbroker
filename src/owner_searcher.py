import json
import time

import requests
from bs4 import BeautifulSoup


# # Replace with your Equasis login details
#
#
# # Start a session to persist cookies
#
# # Get the login page
#
#
# # Print the content of the login page for debugging
#
#
# # Parse the login page
# soup = BeautifulSoup(login_page.content, 'html.parser')
#
# # Locate the correct login form (adjust if needed)
# login_form = soup.find('form', {'name': 'formLogin'}) or soup.find('form', {'name': 'formLoginMobile'})
#
# if login_form is None:
#     print("Login form not found!")
# else:
#     # Extract necessary form data (e.g., hidden inputs)
#     form_data = {}
#     for input_tag in login_form.find_all('input'):
#         if input_tag.get('name'):
#             form_data[input_tag['name']] = input_tag.get('value')
#
#     # Add username and password to the form data
#     form_data['j_email'] = USERNAME
#     form_data['j_password'] = PASSWORD
#
#     # print(form_data)
#     # Send the login request
#
#     imo_number = "9250543"
#
#     ship_search = {
#         'P_IMO': imo_number,
#     }
#     ship_response = session.post(SHIP_INFO, data=ship_search)
#
#     with open("./file.html", "w", encoding='utf-8') as file:
#         file.write(ship_response.text)
#
#     search_soup = BeautifulSoup(ship_response.content, 'html.parser')
#
#     # print(search_soup)
#
#     table = search_soup.find('table', class_='tableLS')
#
#     # print(table)
#
#     # Find all <tr> elements
#     rows = table.find_all('tr')
#     #
#     # print(rows)
#     #
#     # # Loop through each row to find the 'Registered owner'
#
#     result = dict()
#
#     for row in rows:
#         if 'Registered owner' in row.text:
#             print("YES")
#             columns = row.find_all('td')
#             owner_name = columns[2].text.strip()  # Assuming owner name is in the third <td>
#             owner_address = columns[3].text.strip()  # Assuming address is in the fourth <td>
#             # print(f"Owner Name: {owner_name}")
#             # print(f"Address: {owner_address}")
#             # Exit the loop once the registered owner is found
#
#             result = dict(
#                 owner_name=owner_name,
#                 owner_address=owner_address,
#
#             )
#
#             break
#
#     print(json.dumps(result, indent=4))


class OwnerSearcher:
    def __init__(self):
        self.USERNAME = 'sergey.rossman@gmail.com'
        self.PASSWORD = 'Derby777!'
        self.HOME_URL = 'https://www.equasis.org/EquasisWeb/public/HomePage?fs=HomePage&P_ACTION=NEW_CONNECTION'
        self.LOGIN_URL = 'https://www.equasis.org/EquasisWeb/authen/HomePage?fs=HomePage'
        self.DATA_URL = 'https://www.equasis.org/EquasisWeb/restricted/ShipList?fs=ShipName'
        self.SEARCH_URL = 'https://www.equasis.org/EquasisWeb/restricted/Search?fs=Search'
        self.SHIP_INFO = 'https://www.equasis.org/EquasisWeb/restricted/ShipInfo?fs=Search'

        self.session = requests.Session()

        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'Referer': 'https://www.equasis.org/EquasisWeb/public/HomePage?fs=HomePage&P_ACTION=NEW_CONNECTION',
            'Accept-Encoding': 'ggzip, deflate, br, zstd',
            'Content-Type': 'application/x-www-form-urlencoded'
        })

        self.result = dict()
        self.init_session()

    def init_session(self):
        login_page = self.session.get(self.HOME_URL)
        login = self.login()
        print("Login", login)

    def login(self):
        form_data = {
            "j_email": self.USERNAME,
            "j_password": self.PASSWORD
        }
        response = self.session.post(self.LOGIN_URL, data=form_data)

        if "Rossman" in response.text:
            print("VALID LOGIN")
            return True
        else:
            print("INVALID LOGIN")
            return False

    def get_data(self, imo_number):

        time.sleep(1)

        ship_search = {
            'P_IMO': imo_number,
        }
        ship_response = self.session.post(self.SHIP_INFO, data=ship_search)

        # with open("./file.html", "w", encoding='utf-8') as file:
        #     file.write(ship_response.text)

        search_soup = BeautifulSoup(ship_response.content, 'html.parser')

        # print(search_soup)

        table = search_soup.find('table', class_='tableLS')

        if not table:
            print("\n=== RELOGIN ===")
            self.login()
            return self.get_data(imo_number)

        # print(table)

        # Find all <tr> elements
        rows = table.find_all('tr')

        for row in rows:
            if 'Registered owner' in row.text:
                columns = row.find_all('td')
                owner_name = columns[2].text.strip()
                owner_address = columns[3].text.strip()

            if "Ship manager/Commercial manager" in row.text:
                columns = row.find_all('td')
                manager_name = columns[2].text.strip()
                manager_address = columns[3].text.strip()

            if "ISM Manager" in row.text:
                columns = row.find_all('td')
                ism_manager_name = columns[2].text.strip()
                ism_manager_address = columns[3].text.strip()

        result = dict(
            owner=dict(
                name=owner_name,
                address=owner_address,
            ),
            manager=dict(
                name=manager_name,
                address=manager_address,
            ),
            ism_manager=dict(
                name=ism_manager_name,
                address=ism_manager_address,
            )

        )

        return result


if __name__ == "__main__":
    client = OwnerSearcher()

    client.init_session()

    imo_number = "9250543"

    imos = ["9660097", "9250543", "9477490"]

    for number in imos:
        res = client.get_data(number)

        if res:
            print(json.dumps(res, indent=4))
        else:
            print("Nothing")

        print("=====")
