def findOne(newList):
	num = 0
	while newList[num] != 'P':
		num += 1
	return num

def value(newList, standardList):
	num = 15
	sum = 0
	while num > -1:
		sum = sum + abs(ord(newList[num]) - ord(List[num]))
		num = num - 1
	return sum

def valueDirUp(newList, position):
	if position < 4:
		return newList
	else:
		char = newList[position]
		aChar = newList[position - 4]
		newList = newList.replace(char, '1')
		newList = newList.replace(aChar, char)
		newList = newList.replace('1',aChar)
		return newList

def valueDirDown(newList, position):
	if position > 11:
		return newList
	else:
		char = newList[position]
		aChar = newList[position + 4]
		newList = newList.replace(char, '1')
		newList = newList.replace(aChar, char)
		newList = newList.replace('1',aChar)
		return newList

def valueDirRight(newList, position):
	if position == 3 or position == 7 or position == 11 or position == 15:
		return newList
	else:
		char = newList[position]
		aChar = newList[position + 1]
		newList = newList.replace(char, '1')
		newList = newList.replace(aChar, char)
		newList = newList.replace('1',aChar)
		print(newList)
		return newList

def valueDirLeft(newList, position):
	if position == 0 or position == 4 or position == 8 or position == 12:
		return newList
	else:
		char = newList[position]
		aChar = newList[position - 1]
		newList = newList.replace(char, '1')
		newList = newList.replace(aChar, char)
		newList = newList.replace('1',aChar)
		return newList

totalList = []
totalListValue = []
List = "ABCDEFGHIJKLMNOP"
newList_r1 = input()
newList_r2 = input()
newList_r3 = input()
newList_r4 = input()
newList = newList_r1 + newList_r2 + newList_r3 + newList_r4
newList = newList.replace('.','P')
step = 1
while List != newList:
	focus = findOne(newList)
	left = valueDirLeft(newList, focus)
	right = valueDirRight(newList, focus)
	up = valueDirUp(newList, focus)
	down = valueDirDown(newList, focus)
	if left not in totalList:
		totalList.append(left)
		totalListValue.append(value(left,List) + step)
	if right not in totalList:
		totalList.append(right)
		totalListValue.append(value(right,List) + step)
	if up not in totalList:
		totalList.append(up)
		totalListValue.append(value(up,List) + step)
	if down not in totalList:
		totalList.append(down)
		totalListValue.append(value(down,List) + step)
	minN = min(totalListValue)
	where = totalListValue.index(minN)
	newList = totalList[where]
	totalList.pop(where)
	totalListValue.pop(where)
	step = step + 1
print(step-1)











