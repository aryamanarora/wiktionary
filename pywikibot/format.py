import pywikibot, re
from pywikibot import pagegenerators

site = pywikibot.Site()
lemma = pywikibot.Category(site,'Category:Hindi lemmas')

gen_lemma = pagegenerators.CategorizedPageGenerator(lemma)

def correctIPA(wikitext):
    wikitext = re.sub(r"{{IPA\|.+?\|lang=hi}}", "{{hi-IPA}}", wikitext)
    return wikitext

def correctetym(wikitext):
    temp = input("etymology: ")
    wikitext = re.sub(r"{{etyl\|(.+)\|hi}} {{[lm]\|.+\|(.+)}}", "{{der|hi|\1|\2}}", wikitext)

def fixes(wikitext):
    wikitext = correctIPA(wikitext)
    return wikitext
