a = 5;
b = 6;
c = a + b;
print c;

arr = [1,2,3,4,5];
print arr

arr2 = [6,7,8,9,0];
print arr2;

arr3 = arr+arr2;
print arr3;

for i in arr3:
    print i * 2;
    if i < 5:
        print "Less " + `i`;

for j in range(0, len(arr3)):
    #print 'Hi ' + `val` + 'at index  `j`';
    print 'Hi ' + `arr3[j]` + 'at index ' + `j`;

for val,j in zip(arr3, range(len(arr3))):
    #print 'Hi ' + `val` + 'at index  `j`';
    print 'Hi ' + 'val '+`val` + 'at index ' + `j`;

for v,idx in enumerate(arr3):
    print (' FRom enumerate' +  `v` + 'at index ' + `idx`);