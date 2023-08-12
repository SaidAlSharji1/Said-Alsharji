import pandas as pd
from productClass import Product
from StackClass import Stack
#assuming alreadt have data into  exel file into a datafram d
df = pd.read_excel("Reading.xlsx", sheet_name = "products")
print("%20s%20s%10s"%("productName","category","price"))
print("-"*50)
pList = []
productStack = Stack()
for index, row in df.iterrows(): # it will display every row
    productName = row['pName']
    category = row['Category']
    price = row['Price']
    currentProduct = Product(productName, category, price)
    pList.append(currentProduct)
    productStack.push(currentProduct)
    #print(productName," ",category," ", price)
    #print(currentProduct)
    #print(currentProduct.discribtion())
    currentProduct.discount(5)
    #print(f"after : {currentProduct.discribtion()}")
    print("%-20s%-20s%-10.1f"%(productName,category,price))

#outside the loop
print(len(pList))
#outside loop'
print("size of stack", productStack.size())

for p in pList:
    print("%-20s%-20s%-10.1f"%(p.get_name(),p.get_category(),p.get_price()))
print("=================")
while not productStack.is_empty():
    product = productStack.pop()
    print("%-20s%-20s%-10.2f" %(product.get_name(),product.get_category(),product.get_price()))