import re

def email_parse(email_address):
    if re.search(r'\w+@\w+\.\w{2,4}', email_address):
        username, domain = re.split(r'@', email_address)
        return {username: domain}
    else:
        raise ValueError(f'wrong email: {email_address}')

print(email_parse('kostyackova2016@yandex.ru'))