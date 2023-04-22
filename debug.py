data1 = r"C:\Users\user\PycharmProjects\Automation_python\filetest23.txt"
data2 = r"C:\fakepath\filetest23.txt"
print(data1.split('\\')[-1])
print(data2.split('\\')[-1])
assert data1.split('\\')[-1] == data2.split('\\')[-1]
# [-1] - leaving only the file name

