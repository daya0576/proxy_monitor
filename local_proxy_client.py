import requests
from requests.exceptions import ConnectTimeout


def http_get_request(url, proxy=None):
    try:
        response = requests.get(url, proxies=proxy, timeout=1)
        print("done")
        print(
            f"{response.status_code}, {response.elapsed.total_seconds() * 1000:.0f}ms"
        )
    except ConnectTimeout as e:
        print("Failed to connect:", e)
        return None


if __name__ == "__main__":
    # url = "http://cp.cloudflare.com/generate_204"
    # url = "http://www.google.com/generate_204"
    # url = "http://dlercloud.com/"
    url = "http://wifi.vivo.com.cn/generate_204"

    ss = "socks5://:xyzxyz@147.182.204.108:8877"
    # ss = "socks5://:auO7GG60gUqQ@183.240.9.174:42536"
    # ss = "socks5://80.251.218.216:6250"
    shadowsocks_proxy = {"http": ss, "https": ss}

    print("no proxy...")
    response_text = http_get_request(url)
    print("ss proxy...")
    response_text = http_get_request(url, shadowsocks_proxy)
