import requests


def get_url_returned_code(url: str):
    """
    Returns the HTTP code returned when trying to get a page using an URL, or None if it can't connect to the server
    :param url:
    :return:
    """
    try:
        r = requests.get(url)
        return r.status_code
    except:
        return None


def check_subdomain_exist(main_url, subdomain):
    return True if get_url_returned_code(subdomain + '.' + main_url) is not None else False
