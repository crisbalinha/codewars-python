import re

"""
def domain_name(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]
"""

def domain_name(url):
    r = re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url)

    return re.search('(https?://)?(www\d?\.)?(?P<name>[\w-]+)\.', url).group('name')

print(domain_name('http://myhome.geocities.com'))
