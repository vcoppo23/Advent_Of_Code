seats = """BBFFBFBRLL
FFFFBFBRLR
BFFBBFBRLR
"""

indiv_seat = seats.splitlines()
amount = len(indiv_seat)
count = 0
number = []
def check_pass(boardpass):
    boardpass = (boardpass.replace("F", "0"))
    boardpass = (boardpass.replace("L", "0"))
    boardpass = (boardpass.replace("R", "1"))
    boardpass = (boardpass.replace("B", "1"))
    return (int(boardpass,2))

while count <= (amount - 1):
    number.append(check_pass(indiv_seat[count]))
    
    count += 1


def missing_ticket(lst):
    num = 0 
    for i in range(lst[0],lst[-1] + 1):
        print (lst[num], i)
        num += 1
        
       
print (missing_ticket(sorted(number)))
