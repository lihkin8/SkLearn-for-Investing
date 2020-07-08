import urllib.request
import os
import time

path = "E:/intraQuarter"

def Check_Yahoo():
    statspath = path+"/_KeyStats"
    stock_list = [x[0] for x in os.walk(statspath)]
    counter = 0
    
    for e in stock_list[1:]:
        try:
           # print("in")
            e = e.replace("E:/intraQuarter/_KeyStats\\","")
            link = "https://query2.finance.yahoo.com/v10/finance/quoteSummary/"+e.upper()+"?modules=assetProfile,financialData,defaultKeyStatistics,calendarEvents,incomeStatementHistory,cashflowStatementHistory,balanceSheetHistory"
            resp = urllib.request.urlopen(link).read()

            save = "forward_json/"+str(e)+".json"
            store = open(save,"w")
            store.write(str(resp))
            store.close()
            counter +=1
            print("Stored "+ e +".json")
            print("We now have "+str(counter)+" JSON files in the directory.")
           # print("in1")

        except Exception as e:
            print(str(e))
            


Check_Yahoo() 
    
    
