#Sets- Sets are unordered,unique(No duplicates),mutable,can't access by the index.
stu1_mark = {90,82,91,72,66}
stu2_mark = {72,89,92,74,62}

stu1_mark.add(99)
stu1_mark.remove(90)
print(stu1_mark)
print(stu2_mark)
print(stu1_mark | stu2_mark)
print(stu1_mark & stu2_mark)
print(stu1_mark - stu2_mark)
print(stu1_mark ^ stu2_mark)

