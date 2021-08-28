import re

with open('nginx_logs.txt', 'r', encoding='utf-8') as nginx:
    for line in nginx.readlines():
        #93.180.71.3 - - [17/May/2015:08:05:32 +0000] "GET /downloads/product_1 HTTP/1.1" 304 0 "-" "Debian
        result = r'(\d{2,3}\.\d{2,3}\.\d{2,3}\.\d{1,3}) - - \[(\d{2}/\w+/\d{4}:\d\d:\d\d:\d\d \+\d{4})] "(\w+) (/\w+/\w+ \w+/...)" (\d{1,4}) (\d{1,3})'
        my_pr = re.findall(result, line)

print(my_pr)