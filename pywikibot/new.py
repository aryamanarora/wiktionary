import pywikibot, re, csv
from pywikibot import pagegenerators

site = pywikibot.Site('en', 'wiktionary')
site.login()
lemma = pywikibot.Category(site,'Category:Hindi lemmas')

gen_lemma = pagegenerators.CategorizedPageGenerator(lemma)

wikitext = {}
filename = "test.csv"
with open(filename, newline = '') as f:
    reader = csv.DictReader(f)
    for row in reader:
        wikitext[row['word']] = "{{subst:hi-n"
        for key, value in row.items():
            if value: value = re.sub(r'\;\;', '\n', value)
            if key != 'word' and value: wikitext[row['word']] += "|" + key + "=" + value
        wikitext[row['word']] += "}}"
print(wikitext)
for word, text in wikitext.items():
    if not pywikibot.Page(site, word).text:
        page = pywikibot.Page(site, word)
        print(text)
        if input("save? ") == "y":
            page.text = text
            page.save("New Hindi entry (Semi-automated with pywikibot)")
