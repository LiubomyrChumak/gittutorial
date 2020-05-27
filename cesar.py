toDecode = list(input())
k = int(input())
asciiNums = list()
codedList = list()
for el in toDecode:
 asciiNums.append(ord(el))
decodedList = [el-k for el in asciiNums]
for nums in decodedList:
 codedList.append(chr(nums))
codedString = ''.join(codedList)
print(codedString)

