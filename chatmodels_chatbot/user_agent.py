from fake_useragent import UserAgent
import requests

ua = UserAgent()
headers = {"User-Agent": ua.random}

response = requests.get("https://docs.smith.langchain.com/overview", headers=headers)
# print(response.text)