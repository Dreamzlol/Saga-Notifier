import json
import smtplib
import datetime
import time
import requests
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def get_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    divs = soup.find_all(
        'div', {'class': 'teaser3 teaser3--listing teaser-simple--boxed'})
    links = []
    for div in divs:
        id = div.find('a')['href']
        links.append("https://www.saga.hamburg/" + id)
    return links

def load_data(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        return json.load(file)

def save_data(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)

def send_email(sender_email, sender_password, receiver_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print('Sucessfully sent email with new listed objects.')
    except Exception as e:
        print(str(e))

def main():
    url = 'https://www.saga.hamburg/immobiliensuche'
    data = load_data('ids.json')
    existing_links = set(data.get('links', []))
    new_links = set(get_links(url)) - existing_links
    if new_links:
        # Your Credentials
        sender_email = 'denisdsr0@gmail.com' 
        sender_password = 'pghxlbljhdgkprbo'
        receiver_email = 'dreamful92@gmail.com'
        subject = 'SAGA Notify'
        body = 'Hey, I found new objects on SAGA.hamburg, here are the links:\n' + '\n'.join(new_links)
        send_email(sender_email, sender_password, receiver_email, subject, body)
        data['links'] = list(existing_links | new_links)
        save_data(data, 'ids.json')
    else:
        print('Nothing new found. Waiting for next fetch...')

if __name__ == '__main__':
    now = datetime.datetime.now()
    print(f'({now.strftime("%H:%M:%S")}) Starting script...')
    while True:
        main()
        time.sleep(3600) # Wait for one hour before fetching again
