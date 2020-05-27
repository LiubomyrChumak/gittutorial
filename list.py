toDecode = list(input())
k = int(input())
asciiNums = list()
codedList = list()
el = []
for i in toDecode:
 el.append(toDecode)
for x in el:
    if [el] % 2 == 0:
      asciiNums.append(ord(x))
decodedList = [el+k for el in asciiNums]
for nums in decodedList:
 codedList.append(chr(nums))
codedString = ''.join(codedList)
print(codedString)

