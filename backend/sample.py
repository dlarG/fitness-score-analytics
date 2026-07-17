import requests
from bs4 import BeautifulSoup

def print_secret_message_grid(doc_url):
    try:
        # 1. Fetch the HTML content of the public Google Doc
        response = requests.get(doc_url)
        response.raise_for_status()
        
        # 2. Parse HTML to extract the table cells
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        if not table:
            print("Error: No table found in the provided document.")
            return
            
        rows = table.find_all('tr')
        
        grid_data = {}
        max_x = 0
        max_y = 0
        
        # 3. Iterate through rows (skipping the header row)
        for row in rows[1:]:
            cols = row.find_all('td')
            # Ensure the row has the expected 3 columns
            if len(cols) >= 3:
                # Text sanitization to remove non-breaking spaces or trailing artifacts
                x_text = cols[0].get_text(strip=True)
                char = cols[1].get_text()
                y_text = cols[2].get_text(strip=True)
                
                if x_text.isdigit() and y_text.isdigit():
                    x = int(x_text)
                    y = int(y_text)
                    
                    grid_data[(x, y)] = char
                    if x > max_x: max_x = x
                    if y > max_y: max_y = y

        # 4. Print the grid
       
        for current_y in range(max_y, -1, -1):
            row_output = []
            for current_x in range(max_x + 1):
                # Retrieve character or default to a space if empty
                character = grid_data.get((current_x, current_y), ' ')
                row_output.append(character)
            # Join characters together to print the complete row
            print("".join(row_output))
            
    except requests.exceptions.RequestException as e:
        print(f"Network error trying to fetch the document: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


doc_url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"


print_secret_message_grid(doc_url)