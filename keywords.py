
import keyword

#returns full list of python keywords
def keywords():
    list = keyword.kwlist
    #print("No. of keywords present in current version :",
    #len(list))
    return list

#reading python textfile and identifying its keywords
#returns list of python keywords in file
def identifyKeys(txtfile):
    list = keyword.kwlist
    print(list)
    '''with open(txtfile) as f:
        contents = f.read()
        print(contents)'''
    #f = open(textfile, 'r')
    output = []
    with open(txtfile) as f:
        for line in f:
            curr = []
            curr.append(line.strip())
            #print(curr)
            for key in list:
                if any(key in word for word in curr):
                    output.append(key)
            #print(curr)
            #print(line.strip())
    return set(output)
if __name__ == '__main__':
    print(identifyKeys('pythonKeywordTest.txt'))
