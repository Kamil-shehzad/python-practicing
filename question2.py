# list1 = [1, 2, 3, 2, 1]
# list2 = [1, "abc", "abc", 1]


# list1_copy = list1.copy()
# list1_copy.reverse()

# if(list1 == list1_copy ):
#     print('list1 is palindrone')


# list2_copy = list2.copy()
# list2_copy.reverse()


# if(list2 == list2_copy ):
#    print('list2 is palindrone')

# array =["A","F", "G", "B", "C", "D"]

# array.sort()

# print(array)

#Dictionary Practice Question

# dic = {}

# dic["table"] = ["a piece of furniture", "list of  facts and figure"] 
# dic["cat"] = "a small animal"


# Set making

# set = {"python", "java", "C++", "python",  "javascript", "java", "python", "java", "pyhton", "java", "C++", "C"}

# eng_marks = int(input("Enter the marks of English:"))
# urdu_marks = int(input("Enter the marks of Urdu:"))
# math_marks = int(input("Enter the marks of Math:"))

# dic ={}

# dic["english"] = eng_marks
# dic["urdu"] = urdu_marks
# dic["math"] = math_marks

# x = "9.0"
# set ={9, x}


# print(set)

# num = int(input("Enter a number:"))


# i = 1

# while i <= 10:
#     print(num,"X" , i , "=" , num*i)
#     i+= 1

# list = [1,4,9, 16,25,36, 49, 64, 81, 100]
tup = (1,4,9, 16,25,36, 49, 64, 81, 100)

# i = 0

# while i < len(list):
#     print(list[i])
#     i += 1

# num  = int(input("Enter a number: "))

# i = 0

# for el in tup:
#     if el == num:
#         print(el,"is found  at index",i)
        
#     i +=1

# for i in range(1,101):
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# num = int(input("Enter a number: "))

# for i in range(1,11):
#     print(num*i)

# num = int(input("Enter a number: "))
# factorial = 1
# for i in range(1, num+1):
#     factorial *=i
# print(factorial)

def average(a, b, c):
    average = (a+b+c)/3
    return average

ave  = average(5,5,5)
print(ave)