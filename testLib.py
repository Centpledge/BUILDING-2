import StringIO
setA = []
content = 'big\nugly\ncontent\nof\nmultiple\npdf files'
buf = StringIO.StringIO(content)

for a in buf :
    setA.append(a)
print setA[0]
print setA[1]
print setA[2]






