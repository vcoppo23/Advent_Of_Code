question_replies = """abc

a
b
c

ab
ac

a
a
a
a

b
"""
import re
groups = question_replies.split('\n\n')
alpha = [r'a',r'b',r'c',r'd',r'e',r'f',r'g',r'h',r'i',r'j',r'k',r'l',r'm',r'n',r'o',r'p',r'q',r'r',r's',r't',r'u',r'v',r'w',r'x',r'y',r'z']
alpha2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
count = 0
reply_total = 0

def combiner(group):
    group = group.splitlines()
    return ("".join(group))
    

def checker(x, persons):
    letter_lst = []
    print (persons)
    if x > 1:
        x -= 1
    seq = '{' +str(x) + '}'
    for i in range (0,26):

        alpha[i] = alpha[i] + seq
        if re.search(alpha[i],persons):
            letter_lst.append(alpha2[i])
            #print ('found', alpha2[i])
        else:
            pass
            #print ('not', alpha2[i])
        alpha[i] = alpha[i].replace(seq, '')
        
    print (letter_lst)



    
while count <= (len(groups) - 1):
    #print (len(split_groups(groups[count])),split_groups(groups[count]))
    checker(len(combiner(groups[count]))-1,combiner(groups[count]))
    
    count += 1
print (reply_total)
