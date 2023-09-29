#!/usr/bin/python3
""" This module makes a GET request and prints the data """
if __name__ == "__main__":
    from urllib import request

    url = 'https://alx-intranet.hbtn.io/status'
    __type: str = "type: "
    __content: str = "content: "
    __content_utf: str = "utf8 content: "

    with request.urlopen(url) as response:
        if response.getcode() == 200:
            content = response.read()
            __type += str(type(content))
            __content += str(content)
            __content_utf += str(content.decode("utf-8"))

    print(f"Body response:\n\t- {__type}\n\t- {__content}\n"
          f"\t- {__content_utf}")
