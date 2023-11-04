

def ArrayChallenge(arr):
    # code goes here

    arr.sort()
    secMin = arr[1]
    secMax = arr[len(arr) - 2]

    print(secMax, secMin, ":mzx9fklp16")

    print(secMin, secMax)

    return arr


def StringChallenge(strParam):
    # code goes here
    strs = strParam.split("*")
    lst1, lst2 = list(strs[0]), list(strs[1])

    joined = []
    count = 0

    for i in range(0, len(lst1)):
        joined.append(lst1[count])
        joined.append(lst2[count])
        count += 1

    token = 'mzx9fklp16'
    back2str = ''.join([str(item) for item in joined]).strip(' ')

    print(back2str, ":mzx9fklp16")






def main():
    arr = [2,42,42,98]

    ans = ArrayChallenge(arr)

    stringpara = 'aaaa*bbbb'

    ans2= StringChallenge(stringpara)


    print(ans2)
    print(ans)
main()





