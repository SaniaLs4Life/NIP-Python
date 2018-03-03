import numpy as np

def function(nip,weight):
    multiplied = 0
    sum = 0
    remainder = 0
    if(len(nip) == 13):
        for i in nip:
            a = np.array([nip])
            b = np.array([6,5,7,2,3,4,5,6,7])
            np.multiply(a,b)
            multiplied = nip * weight
        print()
        return True
    else:
        return False

    # remainder = sum % 11
    # if(remainder ==  ):
    #     return True
    # else:
    #     return False
#1,2,3,4,5,6,7,8,9,1

def main():
    nip = str(input("Enter xxx-xxx-xx-xx: "))
    weight = str({6,5,7,2,3,4,5,6,7})
    print(function(nip,weight))

if __name__ == '__main__':
    main()

# a = [1,2,3,4]
# b = [2,3,4,5]
# a .* b = [2, 6, 12, 20]

