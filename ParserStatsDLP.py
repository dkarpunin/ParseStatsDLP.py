f = open("db-conn-3.txt", "r").readlines()
h = "dd;keylog_count;keylog_capacity;clipboard_count;clipboard_capacity;removable_count;removable_capacity;exchange_count;exchange_capacity;im_count;im_capacity;printjob_count;printjob_capacity;device_count;device_capacity;email_count;email_capacity;network_count;network_capacity;application_count;application_capacity;file_count;file_capacity_capacity;all_count;all_capacity"
print(h, file=open("db-conn-3.csv", "w"))
l = []
b = "bytes"
kb = "kB"
mb = "MB"
gb = "GB"
for i in f:
    if not i.isspace():
        f = i.replace('\n', '').replace(' ', '').splitlines()
        l += f
del l[0:3]
for i in range(len(l)):
    d = l[i].split('|')
    cc = []
    for j in range(len(d)):
        c = d[j].split('/')
        if any(b in s for s in c):
            e = c[1].replace(b, '')
            e = int(e)
        if any(kb in s for s in c):
            e = c[1].replace(kb, '')
            e = int(e) * 1024
        if any(mb in s for s in c):
            e = c[1].replace(mb, '')
            e = int(e) * 1024 ** 2
        if any(gb in s for s in c):
            e = c[1].replace(gb, '')
            e = int(e) * 1024 ** 3
        if len(c) == 2:
            del c[1]
            c.append(e)
            c[0] = int(c[0])
            for i in range(len(c)):
                cc.append(c[i])
        else:
            cc.append(c[0])
            cc.append('')
    del cc[1]
    print(*cc, sep=";", file=open("db-conn-3.csv", "a+"))