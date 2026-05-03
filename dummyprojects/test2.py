# arr = ["1","this is me","3","4","not me","8"]
 

# for ch in arr:
#     try:
#         if int(ch)%2 == 0:
#             print("True")
#         else:
#             print("False")
#     except:
#         print("False except")
#         continue  

# try:
#     n = 1/0
# except Exception as e:
#     print(e)    


data = {'a': 5, 'b': 9, 'c': 3, 'd': 12}

maxValue = float('-inf')
maxKey = None

for key,value in data.items():
    if value > maxValue:
        maxValue = value
        maxKey = key

print(f'{maxKey} : {maxValue}')        