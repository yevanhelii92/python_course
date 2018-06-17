import webbrowser
import sys


url1 = 'https://github.com/yevanhelii92/python_course'
url2 = 'https://www.google.com.ua'
con = sys.argv[1]
print(con)
def open_link(link):
    if link == '--google':
        webbrowser.open_new(url2)
    elif link == "--github":
        webbrowser.open_new(url1)
    else :
        print ('vvedi norm link')
open_link(con)


