import requests
import datetime

def send_post_request():
    print("Sending request at:", datetime.datetime.now())
    url = 'https://telegram.org/support'
    data = {
        'message': "Dear Sir/Ma'am. MY number +86 134 2923 0959 has been banned and I am not able to figure out the reason for suspension, please help me to recover my account. Thank you.",
        'email': 'eveenfan1206@gmail.com',
        'phone': '+86 134 2923 0959',
        'setln': ''
    }
    
    try:
        response = requests.post(url, data=data)
        print("Status Code:", response.status_code)
        print("Response Headers:", response.headers)
        print("Response Text:", response.text)
        if response.status_code == 200:
            print("Request successful at:", datetime.datetime.now())
        else:
            print("Request failed with status:", response.status_code)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    send_post_request()
