import sys;input=sys.stdin.readline
def isSurprise(string):
    for index in range(1,len(string)-1):
        check_not_sur=set()
        for check_index in range(len(string)-index):
            pair=string[check_index]+string[check_index+index]
            if pair in check_not_sur:
                print(string,"is NOT surprising.")
                break
            else:
                check_not_sur.add(pair)
        else:
            continue
        break
    else:
        print(string,"is surprising.")


while True:
    string=input().rstrip()
    if string=="*":
        break
    else:
        isSurprise(string)

