import requests
from bs4 import BeautifulSoup
import smtplib
import os
from dotenv import load_dotenv
load_dotenv()
EMAIL_ADDRESS =os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD =os.getenv("EMAIL_PASSWORD")
TO_EMAIL_ADDRESS = os.getenv("TO_EMAIL_ADDRESS")
SMTP_ADDRESS = os.getenv("SMTP_ADDRESS")
#PUT THE URL OF THE ITEM WHOSE PRICE YOU WANT TO TRACK
URL="https://www.amazon.in/ASUS-Windows-Graphics-GeForce-GV301QH-K5462TS/dp/B095YTF884?utm_source=chatgpt.com"
headers={
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8,ar;q=0.7,pl;q=0.6",
    "Priority": "u=0, i",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "Windows",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "cross-site",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36 OPR/129.0.0.0",

}
response = requests.get(URL,headers=headers)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

item_title=soup.find("span",id="productTitle").text
item_title=" ".join(item_title.split())
item_price=soup.find("span" ,class_="a-price-whole").text
item_price = item_price.replace(",", "").strip(".")
item_price = int(float(item_price))
target_price=140000
if item_price < target_price:
    with smtplib.SMTP(SMTP_ADDRESS, 587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=EMAIL_PASSWORD)
        connection.sendmail(from_addr=EMAIL_ADDRESS, to_addrs=TO_EMAIL_ADDRESS,
                            msg=f"Subject:PRICE DROP \n\n {item_title} \nprice: {item_price}".encode("utf-8"))