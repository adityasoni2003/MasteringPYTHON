

#Small Method can be usefull to use in some conditions not for all conditions

'''
def Buy8Get1free(No_ofCoffees,Price_PerCoffees):
    No_ofFreeCoffees = No_ofCoffees//9
    No_ofpaidcoffees = No_ofCoffees - No_ofFreeCoffees
    return No_ofpaidcoffees * Price_PerCoffees
print(Buy8Get1free(33,2)) 


'''



#Writing another method to calculate the total price when one coffe is given free when customer buys every 8th coffee


def buy8Get1Free(TotalCoffees,PricePerCoffee):
    totalbuy = 0 
    CoffeeToBuyUntillFree = 8
    while TotalCoffees != 0 :
        CoffeeToBuyUntillFree -= 1
        if CoffeeToBuyUntillFree ==0 :
            CoffeeToBuyUntillFree = 8
        else :
            totalbuy += 1
            CoffeeToBuyUntillFree -= 1 
    return totalbuy * PricePerCoffee
print(buy8Get1Free(5,2))
            