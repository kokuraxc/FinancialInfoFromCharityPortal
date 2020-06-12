import os
import pprint

pp = pprint.PrettyPrinter()
churchs_foler = 'download/christianity/'
all_churchs = os.listdir(churchs_foler)
# pp.pprint(all_churchs)
for c in all_churchs:
    # print(c)
    if os.path.isdir(churchs_foler + c):
        reports = os.listdir(churchs_foler + c + '/')
        if len(reports) == 0:
            print(c)
        # else:
        #     print(c)