set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
print(set1.difference(set2))
print(set2.difference(set1))

data1 = {"test"}
data2 = {1}

data3 = data1.union(data2)
print(data3)



# update


update1 = {"update"}
update2 = {1}

update1.update(update2)
print(update1)