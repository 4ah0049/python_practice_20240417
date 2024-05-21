import random
import pyinputplus as pyip

with open ('names.txt',encoding='utf-8') as file:
    content:str=file.read()

n:int=pyip.inputInt ('請輸入要取得姓名的數量',min=0,max=200)
names:list[str]=content.split(sep='\n')#傳出來是list,是串列資料

random_names:list=random.choices(population=names, k=n)
for name in random_names:
    print(name,end=' ')
print()
