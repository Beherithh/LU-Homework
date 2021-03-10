from tld import get_tld


def get_tl_domain(names: list) -> list:
    return list(map(get_tld, names))


urls = ["http://www.youtube.com", "http://www.estudijas.lu", 'http://www.yandex.ru']
print('Adresses: ', urls)
print('Top level domains: ', get_tl_domain(urls))
