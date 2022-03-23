import requests
import lxml
from bs4 import BeautifulSoup
from smtplib import SMTP

url = "https://www.amazon.co.uk/Elden-Ring-Launch-Edition-PS5/dp/B09L1X8WV3/ref=sr_1_1?crid=3RR0IVWJL17IX&keywords=elden+ring&qid=1647860199&sprefix=el%2Caps%2C382&sr=8-1"
header = {"Accept-Language": "en-US,en;q=0.9", "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Safari/605.1.15", "Cookie": "_ga=GA1.2.1725117867.1647855215; _gid=GA1.2.595032401.1647855215; PHPSESSID=1g5p1dlal2kkntluqtfcrup847"}

response = requests.get(url, headers=header)
webpage = response.text

soup = BeautifulSoup(webpage, "lxml")
price = soup.find("span", class_="a-offscreen")
print(price.getText())

# print(soup.prettify())

with SMTP("GMAIL ADDRESS", port=587) as connection:
    connection.starttls()
    result = connection.login("your_email", "your_password")
    connection.sendmail(
        from_addr="your_email",
        to_addrs="your_email",
        msg=f"subject:Amazon Price Alert!\n\n{message}\n{url}"
    )
