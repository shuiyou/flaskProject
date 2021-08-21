def readtxt():
    f = open("../static/trans_flow_20210411.txt","r")
    line = f.readline()
    line = line[:-1]
    #文件总数据行数
    sumLineNub = 0
    accountSet =()
    while line:
        sumLineNub+=1
        line=f.readline()
        lineDataList =line.split('~@~')
        if lineDataList is None and lineDataList[0]=='':
            continue
        try:
            accountSet =set(accountSet)
            accountSet.add(lineDataList[4])
        except(IndexError):
            print(line)
        line =line[:-1]
    print('潍坊银行流水txt总行数'+str(sumLineNub))
    print('总共出现过的账户数'+str(len(accountSet)))
    f.close()


if __name__ == '__main__':
    readtxt()