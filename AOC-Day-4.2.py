import re
passwords ="""eyr:1972 cid:100
hcl:#18171d ecl:amb hgt:170 pid:186cm  byr:1926

iyr:2019
hcl:#602927 eyr:1967 hgt:170cm
ecl:grn pid:012533040 

hcl:dab227 iyr:2012
ecl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277

hgt:59cm ecl:zzz
eyr:2038 hcl:74454a iyr:2023
pid:3556412378 byr:2007
"""
sep_passwords = passwords.split('\n\n')
count = 0
total = len(sep_passwords)
answer = 0
def term_check(password):
    if (all(i in password fo i in terms)) == True:
        return True
    else:
        return False

def validator(password):
    if password == False:
        return False
    else:
        password
    eyecolor = ['grn','amb', 'blu', 'brn', 'gry', 'hzl', 'oth']
    try:
        byr = re.findall(r'byr\W[0-9]+', password)
    
    except:
        return False
    else:
        if 2002 >= int(byr[0].split(':')[1]) >= 1920:
            pass
        else:
            return False

    try:
        re.search(r'iyr\W[0-9]{4}', password)
    except:
        print ('no')
        return False
    else:
        iyr = re.findall(r'iyr\W[0-9]{4}', password)
        iyr = iyr[0].split(':')
        if 2020 >= int(iyr[1]) >= 2010:
            pass
        else:
            return False
        
    try:
        eyr = re.findall(r'eyr\W[0-9]+', password)
   
    except:
        return False
    else:
        if 2030 >= int(eyr[0].split(':')[1]) >= 2020:
            pass
        else:
            return False
        
    try:
        hgt = re.findall(r'hgt\W\w+', password)

    except:
        return False
    else:
        if  re.search(r'[0-9]+cm',hgt[0].split(':')[1]):
            hgt = hgt[0].split(':')
            hgt = hgt[1].split('c')
            if 193 >= int(hgt[0]) >= 150:
                pass
            else:
                return False
        elif re.search(r'[0-9]+in',hgt[0].split(':')[1]):
             hgt = hgt[0].split(':')
             hgt = hgt[1].split('i')
             if 76 >= int(hgt[0]) >= 59:
                 pass
             else:
                 return False
                
    try:
        re.findall(r'hcl:#[0-9a-f]{6}', password)

    except:
        return False
    else:

        return False
    try:
        ecl = re.findall(r'ecl\W\D{3}', password)

    except:
        return False
    else:
        ecl = ecl[0].split(':')
        if ecl[1] in eyecolor:
            pass
        else:
            return False

    try:
        byr = re.findall(r'pid\W[0-9]{9}', password)

    except:
        return False
    else:
 
        pass
        
    return True

while count <= total - 1:
    if validator(term_check(sep_passwords[count])) == True:
         answer += 1
    else:
        pass
    count += 1
print (answer)
    
    
   
