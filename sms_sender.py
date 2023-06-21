import requests
import json

API_KEY = 'YOUR_API_KEY'
SMS_ENDPOINT = 'https://api.smsmode.com/http/1.6/sendSMS.do'

def send_sms(phone_number, message):
    payload = {
        'apiKey': API_KEY,
        'message': message,
        'numbers': phone_number
    }

    response = requests.post(SMS_ENDPOINT, data=json.dumps(payload), headers={'Content-Type': 'application/json'})

    if response.status_code == 200:
        print('SMS sent successfully!')
    else:
        print('Failed to send SMS.')

def main():
    with open('phone.txt', 'r') as phone_file, open('messages.txt', 'r') as message_file:
        phone_numbers = phone_file.read().splitlines()
        messages = message_file.read().splitlines()

        if len(phone_numbers) != len(messages):
            print('Number of phone numbers does not match number of messages.')
            return

        for phone_number, message in zip(phone_numbers, messages):
            send_sms(phone_number, message)

if __name__ == '__main__':
    main()
