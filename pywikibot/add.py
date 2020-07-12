import pywikibot

site = pywikibot.Site('en', 'wiktionary')
site.login()

with open('add.csv', 'r') as fin:
    for word in fin:
        if not pywikibot.Page(site, word).text:
            print(word)
            input()