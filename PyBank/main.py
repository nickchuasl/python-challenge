import os
import csv


csvpath = os.path.join("Resources","budget_data.csv")

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    
    numberOfMonths = []
    netProfit=0
    
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
    
    #The total number of months included in the dataset
    print(len(numberOfMonths))
    
    #The net total amount of "Profit/Losses" over the entire period
    netProfitformatted = "${:,.2f}".format(netProfit)
    print(netProfitformatted)

    print(len(profitLoss_list))
    
    monthlyChangeList = []
    monthChangePeriod =[]
    
    for i in range(0,(len(profitLoss_list)-1)):
        if i<86:      
            monthlyprofitdiff =0
            monthlyprofitdiff =  float(profitLoss_list[i+1]) - float(profitLoss_list[i])
            monthlyChangeList.append(monthlyprofitdiff)
            changeProfitPeriod = profitPeriod[i+1]
            monthChangePeriod.append(changeProfitPeriod)
    
    #The average of the changes in "Profit/Losses" over the entire period
    averageChange = "${:,.2f}".format(sum(monthlyChangeList)/len(monthlyChangeList))
    print(averageChange)
 
    
    monthlyChange_Dict = {}
    monthlyChange_Dict = {monthChangePeriod[i]: monthlyChangeList[i] for i in range(len(monthlyChangeList))}
    
    #The greatest increase in profits (date and amount) over the entire period
    max_key = max(monthlyChange_Dict,key=monthlyChange_Dict.get)
    all_maxValues = monthlyChange_Dict.values()
    max_values = max(all_maxValues)
    print(max_key)
    maxValuesFormatted = "${:,.2f}".format(max_values)
    print(maxValuesFormatted)
    
    #The greatest decrease in losses (date and amount) over the entire period
    min_key = min(monthlyChange_Dict,key=monthlyChange_Dict.get)
    all_minValues = monthlyChange_Dict.values()
    min_values = min(all_maxValues)
    print(min_key)
    minValuesFormatted = "${:,.2f}".format(min_values)
    print(minValuesFormatted)

#Putting it into a text file in the required format

textpath2 = os.path.join("analysis","financial_analysis.txt")
with open(textpath2, 'a') as summarisedtext:
    summarisedtext.truncate(0)
    summarisedtext.writelines("Financial Analysis\n")
    summarisedtext.writelines("-"*30+"\n")
    summarisedtext.writelines(f"Total Months: {len(numberOfMonths)}\n")
    summarisedtext.writelines(f"Total: {netProfitformatted}\n")
    summarisedtext.writelines(f"Average Change: {averageChange}\n")
    summarisedtext.writelines(f"Greatest Increase in Profits: {max_key} ({maxValuesFormatted})\n")
    summarisedtext.writelines(f"Greatest Decrease in Profits: {min_key} ({minValuesFormatted})\n")
