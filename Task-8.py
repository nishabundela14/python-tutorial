txt=input("Enter text to write to the file: ")
file = open('output.txt', 'w')
file.write(txt + '\n')
print('Data successfully written to output.txt')

txt1=input("Enter additional text to append: ")
file = open('output.txt', 'a')
file.write(txt1 + '\n')
print('Data successfully appended.')

print('Final content of output.txt')
file = open('output.txt', 'r')
data = file.read()
print(data)
    