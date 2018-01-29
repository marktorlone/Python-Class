#program 1 -- CSC 308 -- Python
#Nick Cavalancia, xxx, xxx
#Due Date: Feb. 6, 2018

#get information about stock account from user
name = input("Please enter the stock holder's name: ")
shares = int(input("Please enter the number of shares purchased: "))
pprice = float(input("Please enter the purchase price of each share: "))
sprice = float(input("Please enter the sale price of each share: "))
commission = float(input("Please enter the broker's commission rate (.03 is 3%): "))

#calculations
pcommission = pprice*shares*commission
ptotal = pprice*shares+pcommission
scommission = sprice*shares*commission
stotal = sprice*shares-scommission
profit = stotal - ptotal

#display the information
print ("\n\nStock sales informatation for", name)
print ("-" * 35)
print ("Total Stock Price:\t", end="")
print (format(pprice*shares, '.2f'))                                            #total paid
print ("Purchase Commission:\t", end="")
print (format(pcommission, '.2f'))                                              #Commission when purchased
print ("-" * 35)
print ("Total Spent:\t\t", end="")
print (format(ptotal, '.2f'))
print ("\nTotal Sales:\t\t", end="")
print (format(sprice*shares, '.2f'))                                            #total paid
print ("Sales Commission:\t", end="")
print (format(scommission, '.2f'))                                              #Commission when purchased
print ("-" * 35)
print ("Total Earnings:\t\t", end="")
print (format(stotal, '.2f'))                                                   #net sales saleprice - commission
print ("-" * 35)
print ("Total profit/loss:\t", end="")                                          #display profit/loss
print (format(profit, '.2f'))
