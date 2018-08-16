from urllib.parse import urlparse

#These functions are essential to checking the domain that we are crawling and will not traverse throughout the web uncontrollably

#Get domain name (gets the last two segments of the subdomain)
def get_domain(url):
    try:
        results = get_subdomain(url).split('.')
        return results[-2]+'.'+results[-1]
    except:
        return ''

#Get subdomain name
def get_subdomain(url):
    try:
        return urlparse(url).netloc
    except:
        return ''
