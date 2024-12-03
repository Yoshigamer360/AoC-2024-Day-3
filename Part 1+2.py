totalSum = 0
digits = ['0','1','2','3','4','5','6','7','8','9']
number1 = ''
number2 = ''
doOrDont = 1 #1: do, 0: dont

with open('input.txt', 'r') as f:
    for line in f.readlines():
        index = 0
        lineLength = len(line)
        working = 0
        doOrDontStage = 0
        while index < lineLength:
            if line[index] == 'd':
                doOrDontStage = 1
            elif line[index] == 'o' and doOrDontStage == 1:
                doOrDontStage = 2
            elif line[index] == '(' and doOrDontStage == 2:
                doOrDontStage = 10
            elif line[index] == ')' and doOrDontStage == 10:
                doOrDont = 1
                doOrDontStage = 0
            elif line[index] == 'n' and doOrDontStage == 2:
                doOrDontStage = 3
            elif line[index] == "'" and doOrDontStage == 3:
                doOrDontStage = 4
            elif line[index] == "t" and doOrDontStage == 4:
                doOrDontStage = 5
            elif line[index] == "(" and doOrDontStage == 5:
                doOrDontStage = 6
            elif line[index] == ")" and doOrDontStage == 6:
                doOrDont = 0
                doOrDontStage = 0
            else:
                doOrDontStage = 0

            if line[index] == 'm':
                working = 1
            elif line[index] == 'u' and working == 1:
                working = 2
            elif line[index] == 'l' and working == 2:
                working = 3
            elif line[index] == '(' and working == 3:
                working = 4
                number1 = ''
            elif working == 4:
                if line[index] in digits:
                    number1 += line[index]
                elif line[index] == ',' and number1 != '':
                    working = 5
                    number2 = ''
                else:
                    working = 0
            elif working == 5:
                if line[index] in digits:
                    number2 += line[index]
                elif line[index] == ')' and number2 != '':
                    if doOrDont == 1:
                        totalSum += int(number1) * int(number2)
                        working = 0
                else:
                    working = 0
            else:
                working = 0
            index += 1
            
print(totalSum)
