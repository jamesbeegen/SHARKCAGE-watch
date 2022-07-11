# Get the HTML response of the E-commerce website and write to a file
def get_html():
    import requests
    r = requests.get('https://e-commerce.sscno.nmci.navy.mil/Command/02/ACQ/navbusopor.nsf/97c6ddbb6c3760a288256fab00183536/40a47c61eed04a3b86258703007d995a?OpenDocument&Highlight=0, sharkcage')

    with open('sharkcage.html', 'w') as f:
        f.write(r.text)


# Parse the create HTML file for just the table data which contains the documents
def get_table_length():
    with open('sharkcage.html') as f:
        lines = f.readlines()

    started = False
    for line in lines:
        if "Attachments:" in line:
            started = True
            continue
        if started:
            if ".pdf" in line:
                docs = line
    return len(docs)


# Sends text to verified numbers via twilio
def send_text():
    from twilio.rest import Client 
    numbers = [
        '+15712718255', 
        '+17038015909', 
        '+12103341254', 
        '+15712885538',
        '+19154019419',
        '+7035091311'
        ]
    account_sid = 'redacted' 
    auth_token = 'redacted' 
    client = Client(account_sid, auth_token) 
    
    for number in numbers:
        message = client.messages.create(  
            messaging_service_sid='MGc33520002b302a2275544977e4096dc1', 
            body='Navy E-Commerce site has a new Document Upload',      
            to=number
        ) 


# Main program execution
if __name__ == '__main__':
    import time
    base_len = 7307

    while True:
        get_html()
        if get_table_length() != base_len:
            send_text()
            break
        else:
            time.sleep(120)

    

    
