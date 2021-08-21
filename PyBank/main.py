import os
import csv


csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    #The total number of months included in the dataset
    numberOfMonths = []
    #The net total amount of "Profit/Losses" over the entire period
    netProfit=0
    #The average of the changes in "Profit/Losses" over the entire period
    profitLoss_list = []
    profitPeriod =[]
    csvheader = next(csvreader)
    for row in csvreader:
        separateDates = row[0].split("-")
        months = separateDates[0]
        numberOfMonths.append(months)
        netProfit += float(row[1])
        profitLoss_list.append(row[1])
        profitPeriod.append(row[0])
    print(len(numberOfMonths))
    netProfitformatted = "${:,.2f}".format(netProfit)
    print(netProfitformatted)
    print(len(profitLoss_list))
    
    monthlyChangeList = []
    monthChangePeriod =[]
    #monthlyprofitdiff=0
    #check the formula ensure that it is correct.
    for i in range(0,(len(profitLoss_list)-1)):
    #    print(i)
    #    print(i+1)
        if i<86:       #len(profitLoss_list):
            monthlyprofitdiff =0
            monthlyprofitdiff =  float(profitLoss_list[i+1]) - float(profitLoss_list[i])
            monthlyChangeList.append(monthlyprofitdiff)
            changeProfitPeriod = profitPeriod[i+1]
            monthChangePeriod.append(changeProfitPeriod)
    #print(monthlyChangeList)
    averageChange = "${:,.2f}".format(sum(monthlyChangeList)/len(monthlyChangeList))
    print(averageChange)
    #print(monthChangePeriod)
    
    monthlyChange_Dict = {}
    #print(monthlyChange_Dict)
    
    monthlyChange_Dict = {monthChangePeriod[i]: monthlyChangeList[i] for i in range(len(monthlyChangeList))}
    #print(monthlyChange_Dict)

    max_key = max(monthlyChange_Dict,key=monthlyChange_Dict.get)
    all_maxValues = monthlyChange_Dict.values()
    max_values = max(all_maxValues)
    print(max_key)
    maxValuesFormatted = "${:,.2f}".format(max_values)
    print(maxValuesFormatted)
    
    
    min_key = min(monthlyChange_Dict,key=monthlyChange_Dict.get)
    all_minValues = monthlyChange_Dict.values()
    min_values = min(all_maxValues)
    print(min_key)
    minValuesFormatted = "${:,.2f}".format(min_values)
    print(minValuesFormatted)

#Putting it into a text file in the required format

textpath2 = os.path.join("analysis","financial_analysis.txt")
with open(textpath2, 'a') as summarisedctext:
    summarisedctext.truncate(0)
    summarisedctext.writelines("Financial Analysis\n")
    summarisedctext.writelines("-"*30+"\n")
    summarisedctext.writelines(f"Total Months: {len(numberOfMonths)}\n")
    summarisedctext.writelines(f"Total: {netProfitformatted}\n")
    summarisedctext.writelines(f"Average Change: {averageChange}\n")
    summarisedctext.writelines(f"Greatest Increase in Profits: {max_key} ({maxValuesFormatted})\n")
    summarisedctext.writelines(f"Greatest Decrease in Profits: {min_key} ({minValuesFormatted})\n")
