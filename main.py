import random

#======Customisable Settings========
#How many tickets you buy a week
ticketPerWeek = 2

ticketCost = 2
prizes = [0,ticketCost,30,140,1750,20000000,0]
maxBalls = 49

#=============================

time=0
print("Pick your numbers!")
playerNumbers = [int(input("1-")),int(input("2-")),int(input("3-")),int(input("4-")),int(input("5-")),int(input("6-"))]



totalEarned = 0

matched = 0

l1wins = 0
l2wins =0
l3wins =0
l4wins =0
l5wins =0
l5winsbb =0

l6wins =0
x=0

while l6wins == 0:  
  possibleNumbers = []
  matched = 0
  
  for i in range(1,maxBalls+1):
    possibleNumbers.append(i)
  drawnBalls = []
  for i in range(1,7):
    drawnBall = possibleNumbers[random.randint(1,len(possibleNumbers)) -1]
    if drawnBall in playerNumbers:
      matched = matched+1
    drawnBalls.append(drawnBall)
    possibleNumbers.remove(drawnBall)

  if matched == 1:
    l1wins +=1
  elif matched == 2:
    l2wins +=1
  elif matched == 3:
    l3wins +=1
  elif matched == 4:
    l4wins +=1
  elif matched == 5:
    bonusBall = possibleNumbers[random.randint(1,len(possibleNumbers)) -1]
    if bonusBall in playerNumbers:

      totalEarned = totalEarned + 998250
      l5winsbb +=1
    else:

      l5wins +=1
  elif matched == 6:
      l6wins += 1

  totalEarned = totalEarned + prizes[matched-1]
  x+=1
  if x%10000 == 0:
    print ("\n" * 50)
    print("-----------",round((x/ticketPerWeek)/52,1),"years-------------")
    print("1 Ball:\t", l1wins , "= £", l1wins * prizes[0], "    \t1 in", round(x/(l1wins+1)))
    print("2 Ball:\t", l2wins , "= £", l2wins * prizes[1], "    \t1 in", round(x/(l2wins+1)))
    print("3 Ball:\t", l3wins , "= £", l3wins * prizes[2], "    \t1 in", round(x/(l3wins+1)))
    print("4 Ball:\t", l4wins , "= £", l4wins * prizes[3], "    \t1 in", round(x/(l4wins+1)))
    print("5 Ball:\t", l5wins , "= £", l5wins * prizes[4], "    \t1 in", round(x/(l5wins+1)))
    print("5Bonus:\t", l5winsbb, "= £",l5winsbb *1000000, "     \t    1 in", round(x/(l5winsbb+1)))
    print("6 Ball:\t", l6wins, "= £", l6wins * prizes[5], "     \t\t1 in", round(x/(l6wins+1)))
    print("---------------------------------")
    print("Tickets:", x,"\tSpent:£",x*ticketCost,"\tEarned:£",totalEarned, "\tProfit:£", (-(x*ticketCost - totalEarned)))
    print("---------------------------------\n")


print ("\n" * 50)

print(drawnBalls)
print(playerNumbers)
print("-----------",round((x/ticketPerWeek)/52,1),"years-------------")
print("1 Ball:\t", l1wins , "= £", l1wins * prizes[0], "    \t1 :", round(x/(l1wins+1)))
print("2 Ball:\t", l2wins , "= £", l2wins * prizes[1], "    \t1 :", round(x/(l2wins+1)))
print("3 Ball:\t", l3wins , "= £", l3wins * prizes[2], "    \t1 :", round(x/(l3wins+1)))
print("4 Ball:\t", l4wins , "= £", l4wins * prizes[3], "    \t1 :", round(x/(l4wins+1)))
print("5 Ball:\t", l5wins , "= £", l5wins * prizes[4], "    \t1 :", round(x/(l5wins+1)))
print("5Bonus:\t", l5winsbb, "= £",l5winsbb *1000000, "     \t1 :", round(x/(l5winsbb+1)))
print("6 Ball:\t", l6wins, "= £", l6wins * prizes[5], "     \t1 :", round(x/(l6wins+1)))
print("---------------------------------")
print("Tickets:", x,"\tSpent:£",x*ticketCost,"\tEarned:£",totalEarned, "\tProfit:£", (-(x*ticketCost - totalEarned)))
print("---------------------------------\n")

totalSpent = x*ticketCost
profit = -(totalSpent - totalEarned)
print("£"+ str(totalEarned)+" total prize!")
print("Wow! You have earned £",profit, "in", x, "tickets!")