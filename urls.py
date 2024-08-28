import requests
from urllib.parse import urlparse
import log

dnsmasq_2_86_prefix = 'local=/'
dnsmasq_2_85_prefix = 'server=/'
dnsmasq_postfix = '/'
hosts_prefix = '0.0.0.0 '

def lines_to_urls(lines, simple):
    urls = []
    for line in lines:
        if line.startswith('#'): 
            continue
        elif simple:
            urls.append(line.rstrip())
        elif line.startswith(dnsmasq_2_86_prefix):
            urls.append(line[len(dnsmasq_2_86_prefix):-len(dnsmasq_postfix)])
        elif line.startswith(dnsmasq_2_85_prefix):
            urls.append(line[len(dnsmasq_2_85_prefix):-len(dnsmasq_postfix)])
        elif line.startswith(hosts_prefix):
            urls.append(line[len(hosts_prefix):])
        elif urlparse(line).netloc != '':
            urls.append(line.rstrip())
    return urls

def read_from_file(file):
    return lines_to_urls(file.readlines(), True)

def read_from_remote(remote):
    urls = []
    res = requests.get(remote)
    if res.status_code == 200:
        lines = res.text.split('\n')
        urls = lines_to_urls(lines, False)
    return urls

def to_lines(blacklist, whitelist, omit, method):
    lines = []
    for url in blacklist:
        line = ''
        if whitelist is not None:
            if url in whitelist:
                if omit:
                    continue
                line = '#'
        if method == 0:
            line += dnsmasq_2_86_prefix + url + dnsmasq_postfix
        elif method == 1:
            line += dnsmasq_2_85_prefix + url + dnsmasq_postfix
        elif method == 2:
            line += hosts_prefix + url
        elif method == 3:
            line += url
        if len(line) > 1:
            lines.append(line)
    return lines
        