
m=[]
a=['TIME', 'DESCRIPTION', 'TEMP', 'FEELS', 'PRECIP', 'HUMIDITY', 'WIND']
a.insert(1,"DAY")
b=','.join(a)
b=b.replace(','," ")
m.append(b)
print(m)