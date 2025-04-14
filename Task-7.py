try:
    file = open('sample.txt', 'r')
    filecontent = file.read()
    print(filecontent)
except:
    print("The file 'sample.txt' was not found")
    
    
