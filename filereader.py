# My exersices in reading files

#open
f = open('names.txt', 'rw')
org = f.read().split()
list1 = []
list2 = []
for name in org:
    if "+" in name:
        list1.append(name)
        print name,
    else:
        list2.append(name)
        print name,
list0 = list1 + list2
print list0
f = open('names.txt', 'rw')
for item in list0:
    f.write("%s" % item)
f.close()
