word = input("단어를 입력하세요 : ")
print(word.isalpha())
print(word.isalnum())
print(word.isupper())
print(word.islower())
print("@" in word)

file_name = input("파일명을 입력하세요 : ")
print(file_name.endswith(".text"))
print(file_name.endswith(".jpg"))
print(file_name.endswith(".py"))