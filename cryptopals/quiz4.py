# coding=utf-8

def get_score(line):
    score = 0
    for letter in line:
        if 'a'<=letter<='z' or 'A'<=letter<='Z' or letter == ' ':
            score += 1
    if score:
        return float(score) / len(line)
    return 0
 
f = open('4.txt')
lastresult = []
lastresult.append('')
lastresult.append('')
lastresult.append('')
while 1:
    nowline = f.readline().strip().decode('hex')
    if nowline == '':
        break
    result = []
    result.append('')
    result.append('')
    result.append('')
    for i in range(0,256):
        line = ''
        for letter in nowline:
            line += chr(ord(letter)^i)
        if get_score(result[0]) < get_score(line):
            result[0] = line
            result[1] = nowline
            result[2] = i
            
    if get_score(lastresult[0]) < get_score(result[0]):
        lastresult[0] = result[0]
        lastresult[1] = result[1]
        lastresult[2] = result[2]
        
print lastresult, get_score(lastresult[0])

# 7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f
# 5
# Now that the party is jumping\n
