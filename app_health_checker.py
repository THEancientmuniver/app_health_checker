import requests

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"The application is UP. Status code: {response.status_code}")
        else:
            print(f"The application is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"The application is DOWN. Error: {e}")

# Replace with your application's URL
application_url = 'http://localhost:3000'
check_application_health(application_url)
