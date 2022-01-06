from fake_useragent import UserAgent

ua = UserAgent()

super_prop = "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6InBsLVBMIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzk2LjAuNDY2NC40NSBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiOTYuMC40NjY0LjQ1Iiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL3d3dy5nb29nbGUuY29tLyIsInJlZmVycmluZ19kb21haW4iOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmUiOiJnb29nbGUiLCJyZWZlcnJlcl9jdXJyZW50IjoiaHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8iLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiJ3d3cuZ29vZ2xlLmNvbSIsInNlYXJjaF9lbmdpbmVfY3VycmVudCI6Imdvb2dsZSIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjEwNTY5MSwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0="
cookie = "__dcfduid=3e21c4e04d4711ecb7477dc970b8d78a; __sdcfduid=3e21c4e14d4711ecb7477dc970b8d78a3373b4ed2b5eddf5b5d8e0e2db9231ba7440e51838dd069407d6a32711213116; locale=pl; OptanonAlertBoxClosed=2021-11-24T20:14:32.792Z; OptanonConsent=isIABGlobal=false&datestamp=Wed+Nov+24+2021+21%3A14%3A32+GMT%2B0100+(czas+%C5%9Brodkowoeuropejski+standardowy)&version=6.17.0&hosts=&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1&AwaitingReconsent=false; _gcl_au=1.1.1799956091.1637784873; _ga=GA1.2.328569601.1637784873; _gid=GA1.2.722956552.1637784873; _gat_UA-53577205-2=1"


class Header:
    def __init__(self, authorization, method, lang):
        self.token = authorization
        self.method = method
        self.lang = lang
        self.header = None
        self.user_agent = ua.random

    def refresh_ua(self):
        self.user_agent = ua.random

    def create_header(self, url):
        self.header = {
            "authority": "discord.com",
            "method": self.method,
            "path": url,
            "sheme": "https",
            "accept": "*/*",
            # "accept-encoding" : "gzip, deflate, br",
            "accept-language": self.lang,
            "authorization": self.token,
            'cookie': cookie,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "x-debug-options": "bugReporterEnabled",
            'x-super-properties': super_prop,

        }

    def create_post_header(self, url):
        self.header = {
            "authority": "discord.com",
            "method": self.method,
            "path": url,
            "sheme": "https",
            "accept": "*/*",
            # "accept-encoding" : "gzip, deflate, br",
            "accept-language": self.lang,
            "authorization": self.token,
            "content-type": "application/json",
            'cookie': cookie,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "x-debug-options": "bugReporterEnabled",
            'x-super-properties': super_prop,

        }

    def typing_header(self, url, length):
        self.header = {
            "authority": "discord.com",
            "method": self.method,
            "path": url,
            "sheme": "https",
            "accept": "*/*",
            # "accept-encoding" : "gzip, deflate, br",
            "accept-language": self.lang,
            "authorization": self.token,
            "content-length": str(length),
            "content-type": "application/json",
            'cookie': cookie,
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': "Windows",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "x-debug-options": "bugReporterEnabled",
            'x-super-properties': super_prop,

        }
