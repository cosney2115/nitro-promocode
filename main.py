import requests,threading,user_agent,uuid,random

class NitroGenerator:
    def __init__(self):
        self.useragent = user_agent.generate_user_agent()
        self.proxy_format = self.proxy()

    def proxy(self):
        proxy_list = open("proxy.txt", "r").read().splitlines()
        proxy = random.choice(proxy_list)
        proxy_format = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}"
        }
        return proxy_format
    
    def generate_nitro(self):
        try:
            headers = {
                'authority': 'api.discord.gx.games',
                'accept': '*/*',
                'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
                'content-type': 'application/json',
                'origin': 'https://www.opera.com',
                'referer': 'https://www.opera.com/',
                'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'cross-site',
                'user-agent': self.useragent,
            }

            json_payload = {
                'partnerUserId': str(uuid.uuid4()),
            }

            response = requests.post('https://api.discord.gx.games/v1/direct-fulfillment', headers=headers, json=json_payload, proxies=self.proxy_format)
            token = response.json()['token']

            nitro_link = "https://discord.com/billing/partner-promotions/1180231712274387115/" + token
            print(nitro_link)
            open("nitro.txt", "a").write(nitro_link + "\n")
        except Exception:
            pass

    def start(self):
        while True:
            self.generate_nitro()

if __name__ == "__main__":
    generator = NitroGenerator()
    for i in range(100):
        threading.Thread(target=generator.start).start()
