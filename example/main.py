import requests

# 대상 URL
url = 'https://www.google.com'

def main():
    response = requests.get(url)
    print(f"<response status_code={response.status_code} text={response.text}>")


if __name__ == "__main__":
    main()
