import os
import pprint

pp = pprint.PrettyPrinter()
churchs_foler = 'Churchs/'
all_churchs = os.listdir(churchs_foler)
# pp.pprint(all_churchs)
for c in all_churchs:
    reports = os.listdir(churchs_foler + c + '/')
    if len(reports) == 0:
        print(c)
    # else:
    #     print(c)