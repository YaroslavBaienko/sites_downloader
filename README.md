# Supreme Court Document Downloader

This script is designed to download PDF documents from the Supreme Court of Ukraine's website. It checks for the existence of specific PDF files and downloads them if they exist.

## Features

- Checks for the existence of PDF files based on a naming pattern.
- Downloads the existing PDF files.
- Pauses for 1 second between each request to avoid overwhelming the server.

## Requirements

- Python 3.x
- `requests` library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/YaroslavBaienko/sites_downloader.git
   ```

2. Navigate to the repository directory:
   ```
   cd /sites_downloader
   ```

3. Install the required libraries:
   ```
   pip install requests
   ```

## Usage

1. Run the script:
   ```
   python main.py
   ```

2. The script will check for the existence of PDF files and download them if they exist. The downloaded files will be saved in the same directory as the script.

## Configuration

- `URL`: The base URL where the PDF files are hosted.
- `symbols`: The number of possible PDF files you want to check. For example, if you set `symbols` to 372, the script will check for files named `St_0.pdf` to `St_371.pdf`.

## Contribution

Feel free to fork this repository and submit pull requests. All contributions are welcome!

## License

This project is licensed under the MIT License.


```
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
```
