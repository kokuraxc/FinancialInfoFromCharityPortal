import os

printed = os.listdir('D:/GH/backup/pdf_saves/')
# print(printed)
printed_churches = []
for p in printed:
    _p = p[:-7]  # + p[-4:]
    if _p not in printed_churches:
        printed_churches.append(_p)

print(printed_churches)
print(len(printed_churches))

with open('christianity - Copy.txt', 'r') as all_churches:
    for c in all_churches:
        _c = ' '.join(c.split())
        if _c not in printed_churches:
            print(_c)