from fake_useragent import UserAgent

def get_custom_user_agent():
    ua = UserAgent()
    tries = 0
    max_tries = 10 

    while tries < max_tries:
        user_agent = ua.chrome
        if ("Macintosh" in user_agent or "X11; Linux" in user_agent):
            return user_agent
        tries += 1

    return "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"


