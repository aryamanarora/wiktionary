import pywikibot

site = pywikibot.Site(code='en', fam='wiktionary')
site.login()

# with open('assamese.txt', 'r') as fin:
#     for line in fin:
#         title = 'Category:' + line.strip('\n')
#         newtitle = title.replace('Old Assamese', 'Early Assamese')
#         page = pywikibot.Page(site, title)
#         page.move(
#             newtitle,
#             reason="replace Old Assamese with Early Assamese",
#             movetalk=True,
#             noredirect=False
#         )

for page in pywikibot.Category(site, "Category:Old Assamese lemmas").articles():
    page.text = page.text.replace("Old Assamese", "Early Assamese")
    page.save("replace Old Assamese with Early Assamese")