from bs4 import BeautifulSoup
import urllib.request

total_pages = 5570
with open("dasa_list.txt", "a") as fout:
    for page in range(1, total_pages + 1):
        print(page)
        link = "https://dsalsrv04.uchicago.edu/cgi-bin/app/dasa-hindi_query.py?page=" + str(page)
        with urllib.request.urlopen(link) as resp:
            soup = BeautifulSoup(resp, 'html.parser')
            for s in soup.find_all("hw"):
                s.extract()
                fout.write(str(s.find('b'))[3:-4])
