import pywikibot

site = pywikibot.Site(code='en', fam='wiktionary')

def no_declension():
    nouns = list(pywikibot.Category(site, "Category:Hindi nouns").articles())
    nouns_with_decl = list(pywikibot.Category(site, "Category:Hindi nouns with declension").articles())
    print(list(set(nouns) - set(nouns_with_decl)))