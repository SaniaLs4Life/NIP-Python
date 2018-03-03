import numpy as np

def function(nip):
    if(len(nip) == 13):
        result = True
    else:
        result = False
    if(result):
        newNip = nip.replace("-", "")
        weight = {6, 5, 7, 2, 3, 4, 5, 6, 7}
        lastDigit = newNip[-1]
        for i in int(range(newNip)):
            num = newNip[i]
            w = weight[i]

            total = num * w
            sum += total
        remainder = sum % 11
        if(remainder == lastDigit):
            result = True
        else:
            result = False
    return result


    # remainder = sum % 11
    # if(remainder ==  ):
    #     return True
    # else:
    #     return False
#1,2,3,4,5,6,7,8,9,1

def main():
    nip = input("Enter xxx-xxx-xx-xx: ")
    print(function(nip))

if __name__ == '__main__':
    main()

# a = [1,2,3,4]
# b = [2,3,4,5]
# a .* b = [2, 6, 12, 20]

