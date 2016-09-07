#coding=utf-8
data1 = "MEMATRHTGPRYETEFETEOAAT "
length =  len(data1)
for i in xrange(2,length):
    if length%i==0:
        s = ""
        for j in range(i):
            for m in range(j,length,i):
                s = s+data1[m]
        # if "wctf" in s:
        #     print s
        print s.lower()