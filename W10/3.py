import requests


def status_code(url: str):
    try:
        result = requests.get(url).status_code
    except requests.ConnectionError:
        result = "failed to connect"
    except:
        result = "wrong url"
    return result


adr = input("Enter address: ")
print(status_code(adr))


