# import random
#
# # Determinestic Inputs
# ShortageCost = 100
# HoldingCost = 50
# SellingPrice = 450
#
# # lists
# profitlist = list()
# x= list()          #Demands
#
# def random_0to1():
#     return random.uniform(0, 1)
#
# def get_x():
#   rand_prob=random_0to1()
#   if rand_prob>=0 and rand_prob<0.2:
#        x=0
#   elif rand_prob>=0.2 and rand_prob<0.6:
#        x=1
#   elif rand_prob>=0.6 and rand_prob<0.8:
#        x=2
#   elif rand_prob>=0.8 and rand_prob<0.9:
#        x=3
#   else :
#        x=4
#   return x
#
# for i in range (500) :      #i is the Order
#     x.append(get_x ())
#
# for Order in range (1,3) :         #Order is 1 or 2
#     Available = 0
#     for Week in range (500) :   #500 Week
#         Available += Order
#         if x[Week]< Available :
#             sold = x[Week]
#             Available -= x[Week]
#             loss = Available * HoldingCost
#         elif x[Week] > Available :
#             sold = Available
#             Available = 0
#             loss = (x[Week] - sold) * ShortageCost
#         else :
#             sold = x[Week]
#             Available = 0
#             loss = 0
#         revenue = sold * SellingPrice
#         profit = revenue - (loss)
#         #if profit >= 0 :
#         profitlist.append(profit)
#     if Order == 1 :
#         AverageProfit1 = sum(profitlist) / 500
#         profitlist.clear()
#     else :
#         AverageProfit2 = sum(profitlist) / 500
#
#
# # Printing Information:
#
# print ("The average profit of 500 weeks :" , "\n")
# print ("if the shop owner ordered 1 PC per week :" , AverageProfit1 ,"\n" )
# print ("if the shop owner ordered 2 PC per week :" , AverageProfit2 ,"\n" )
#
# if AverageProfit1 > AverageProfit2 :
#     print("Ordering 1 PC per week is the best decision")
# elif AverageProfit1 < AverageProfit2:
#     print("Ordering 2 PC per week is the best decision")


import random
import matplotlib.pyplot as plt

# Deterministic Inputs
ShortageCost = 100
HoldingCost = 50
SellingPrice = 450

# Lists
profitlist = []
x = []  # Demands


def random_0to1():
    return random.uniform(0, 1)

def get_x():
    rand_prob = random_0to1()
    if rand_prob >= 0 and rand_prob < 0.2:
        x = 0
    elif rand_prob >= 0.2 and rand_prob < 0.6:
        x = 1
    elif rand_prob >= 0.6 and rand_prob < 0.8:
        x = 2
    elif rand_prob >= 0.8 and rand_prob < 0.9:
        x = 3
    else:
        x = 4
    return x


for i in range(500):  # i is the Order
    x.append(get_x())

for Order in range(1, 3):  # Order is 1 or 2
    Available = 0
    profitlist = []  # Create a new profitlist for each strategy
    for Week in range(500):  # 500 Weeks
        Available += Order
        if x[Week] < Available:
            sold = x[Week]
            Available -= x[Week]
            loss = Available * HoldingCost
        elif x[Week] > Available:
            sold = Available
            Available = 0
            loss = (x[Week] - sold) * ShortageCost
        else:
            sold = x[Week]
            Available = 0
            loss = 0
        revenue = sold * SellingPrice
        profit = revenue - loss
        profitlist.append(profit)

    if Order == 1:
        AverageProfit1 = sum(profitlist) / 500
    else:
        AverageProfit2 = sum(profitlist) / 500

# Print the average profit for each strategy
    if Order == 1:
        print("The average profit of 500 weeks if the shop owner ordered 1 PC per week:", AverageProfit1)
    else:
        print("The average profit of 500 weeks if the shop owner ordered 2 PC per week:", AverageProfit2)

# histogram for the profit distribution
    plt.hist(profitlist, bins=20, label=f"Order {Order} PC/week")
    plt.xlabel("Profit")
    plt.ylabel("Frequency")
    plt.legend()
# console printing
if AverageProfit1 > AverageProfit2:
    print("Ordering 1 PC per week is the best decision")
elif AverageProfit1 < AverageProfit2:
    print("Ordering 2 PC per week is the best decision")

plt.show()
