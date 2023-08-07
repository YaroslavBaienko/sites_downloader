import requests
import time

URL = "https://supreme.court.gov.ua/userfiles/media/new_folder_for_uploads/supreme/"

def check_existing(URL, symbols: int):
    existing = []

    for i in range(0, symbols):
        last_address = f"St_{i}.pdf"
        current_url = f"{URL}{last_address}"

        try:
            response = requests.get(current_url)
            if response.status_code == 200:
                existing.append((response.status_code, current_url))
                filename = current_url.split("/supreme/")[1]
                with open(filename, "wb") as file:
                    file.write(response.content)
            time.sleep(1)  # pause for 1 second between requests
        except requests.RequestException as e:
            print(f"Error for URL {current_url}: {e}")

    return existing

print(check_existing(URL=URL, symbols=372))
