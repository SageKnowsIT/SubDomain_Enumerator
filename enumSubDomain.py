import requests

domain = "ENTER-DOMAIN-HERE.com"
subDom = ['www', 'mail', 'ftp', 'blog', 'webmail', 'server', 'ns1', 'ns2', 'smtp', 'secure', 'test', 'cpanel', 'whm', 'admin', 'forum', 'shop', 'store', 'api', 'dev', 'docs', 'support', 'web', 'portal', 'beta', 'demo', 'stats', 'm', 'cdn', 'img', 'static', 'news', 'media', 'my', 'chat', 'community', 'dashboard', 'home', 'login', 'signup', 'app', 'site', 'services', 'files', 'downloads', 'video', 'videos', 'content', 'events', 'jobs']
for s in subDom:
    url = f"https://{s}.{domain}"
    try:
        # Check Status Code of Domain
        # Enumerate subdomains
        response = requests.get(url)
        # Print Status Code
        #print(response.status_code)
        print(f'{url} is a valid domain.')

        # Close Connection

        #response.close()
        #print("Connection Closed")


    except requests.exceptions.RequestException as e:
        # Print error message if an exception occurs
        #print(f"An error occurred: {e}")
        pass



