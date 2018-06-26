import webbrowser
import sys


con = sys.argv
print(con)
# browser, url = con[1], con[2]
browser = con[1]
url = con[2]
print(browser)
print(url)


def open_link_in_browser(browser, url):
    if browser == 'chrome'or browser == 'firefox':
        webbrowser.get(browser).open(url)
    else :
        print ("Yandex doesn't work in Ukraine")


open_link_in_browser(browser, url)
