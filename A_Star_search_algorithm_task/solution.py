def heuristicDictBuilder(givenInput):
    heuristicDict = {}
    for i in givenInput:
        eachLine = i.split(' ')
        heuristicDict[eachLine[0]] = int(eachLine[1])
    return heuristicDict


def priorityQueueBuilder(stackList):
    for i in range(len(stackList)-1):
        for j in range(i+1, len(stackList)):
            if stackList[i][1] < stackList[j][1]:
                temp = stackList[i]
                stackList[i] = stackList[j]
                stackList[j] = temp
    return stackList


def ifExistLower(stckList, node):
    flag = False
    for i in stckList:
        if i[0] == node[0] and i[1] <= node[1]:
            flag = True
            return flag
    return flag


def aStarAlgo(givenInput, heuristicDict, startNode, endNode):
    priorityQueue = []
    visitedNode = []
    priorityQueue.append([startNode, heuristicDict[startNode], startNode])
    while len(priorityQueue) > 0:
        popedNode = priorityQueue.pop()
        if popedNode[0] == endNode:
            return [popedNode[2], popedNode[1]-heuristicDict[popedNode[0]]]
        for i in givenInput:
            temp = i.strip().split(' ')

            if temp[0] == popedNode[0]:
                for j in range(2, len(temp), 2):
                    pathCost = int(temp[j+1])+popedNode[1]-heuristicDict[popedNode[0]]+heuristicDict[temp[j]]
                    if ifExistLower(visitedNode, [temp[j], pathCost]) == False:
                        priorityQueue.append(
                            [temp[j], pathCost, (popedNode[2]+'->'+temp[j])])
                        visitedNode.append([temp[j], pathCost])
                        priorityQueue = priorityQueueBuilder(priorityQueue)
                break


def outputGenerator(result, outputFile):
    outputText = ''
    outputText += 'Path: '+ result[0]+'\n'
    outputText += 'Total distance: '+ str(result[1])+ 'km'
    # print('Path: ', result[0])
    # print('Total distance: ', result[1], 'km')
    outputFile.write(outputText)


def inputFormatter(givenInput):
    mIndx = 0
    indx = 0
    while mIndx < len(givenInput):
        val = ord(givenInput[mIndx][indx])
        if (val < 65 or val > 90) and (val < 97 or val > 122):
            indx += 1
        else:
            if indx > 0:
                givenInput[mIndx] = givenInput[mIndx][indx:]
            indx = 0
            mIndx += 1
    return givenInput

if __name__ == "__main__":
    f = open("input_output_files\Input file.txt", "r")
    outputFile = open("input_output_files\output_file.txt","w")
    givenInput = f.read().split('\n')
    formattedInput = inputFormatter(givenInput)
    heuristicDict = heuristicDictBuilder(formattedInput)
    start_node = 'Arad'
    end_node = 'Bucharest'
    if start_node in heuristicDict and end_node in heuristicDict:
        result = aStarAlgo(formattedInput, heuristicDict, start_node, end_node)
        outputGenerator(result,outputFile)
    else:
        # print('Start or End node doesn\'t exists')
        outputFile.write('Start or End node doesn\'t exists')
