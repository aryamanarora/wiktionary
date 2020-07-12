import pywikibot

site = pywikibot.Site(code='en', fam='wiktionary')
site.login()

def no_declension():
    nouns = list(pywikibot.Category(site, "Category:Hindi nouns").articles())
    nouns_with_decl = list(pywikibot.Category(site, "Category:Hindi nouns with declension").articles())
    print(list(set(nouns) - set(nouns_with_decl)))

def check():
    counts = {}
    with open('freq.csv') as fin:
        line = fin.readline()
        i = 0
        while line:
            if i % 100000 == 0:
                print(i)
            try:
                x = line.strip().split(',')
                counts[x[0]] = int(x[1])
                line = fin.readline()
            except:
                print(line)
            i += 1
    counts = sorted(counts.items(), key=lambda kv: -kv[1])
    exist = set(pywikibot.Category(site, "Category:Hindi lemmas").articles())
    other = set(pywikibot.Category(site, "Category:Hindi non-lemma forms").articles())
    exist = exist | other
    with open('freq2.csv', 'w') as fout:
        for word, freq in counts:
            fout.write(word + ',' + str(freq) + '\n')


if __name__ == "__main__":
    check()