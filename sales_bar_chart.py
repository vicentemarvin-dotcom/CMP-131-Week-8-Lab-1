ast="*"
store=int(input("enter number of stores"))
for i in range (store):
    sales=int(input("Enter today store "+str((i+1))+" : "))
    store=str(ast)
    sales=sales/100
    sales=int(sales)
    for j in range(sales):
        ast=ast+"*"
    ast=ast+"\n"
print(ast)