import browser_cookie3
import requests
import traceback

DOMAIN_NAME = "adventofcode.com"


def get_cookies_from_chrome():
    try:
        cookies = dict()
        cookie_jar = browser_cookie3.chrome(domain_name=DOMAIN_NAME)
        for cookie in cookie_jar:
            cookies[cookie.name] = cookie.value
        return cookies
    except Exception as exc:
        traceback.print_exception(exc)


def get_url(url, timeout=1.0, cookies=None):
    try:
        kwargs = {"timeout": timeout}
        if cookies is not None:
            kwargs["cookies"] = cookies
        return requests.get(url, **kwargs)
    except Exception as exc:
        traceback.print_exception(exc)
        pass
