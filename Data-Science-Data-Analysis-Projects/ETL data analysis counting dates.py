"""
Input files are a csv file of prices (pricelist) and 3 csv files with data about 
sales and warranty of 6 different models.  Sales files have similar data 
in a different order and 15 to 20 columns depending on the file,
and no two files are the same.
Sales files have warranty dates, which is used to calculate when warranty ends.
Price list has prices that depend on the product license.  In this case, only
the 1 year product license prices are needed.  One column lists in a string
both the model and the license length.
Program counts how many warranties end in a particular month for each model
in 2018 and multiplies the number by the net price.
Output file has columns make, model, and months of the year.
"""

import csv
from datetime import datetime as dt
import datetime
import calendar

def read_csv(filename):
    with open(filename, 'rt') as f:
        reader = csv.DictReader(f)
        return list(reader)
    
def fix_dates(modelx):
    for x in modelx:
        if (x['Warranty'] != '') and ('n/a' not in x['Warranty']):            
            if (x['Warranty'][-3] == '/'):
                paddedy = '20' + x['Warranty'][-2:]
                paddedw = x['Warranty'][:-2] + paddedy
                x['Warranty'] = paddedw
            newdatetime = dt.strptime((x['Warranty']),'%m/%d/%Y')
            newdate = dt.date(newdatetime)
            x['Warranty'] = newdate
            
def initialize_months():
    init = {}
    for i in range(1,13):
        init[calendar.month_abbr[i]] = 0
    return init
    
def count_dates_for_models(modelx, model):
    monthcounts = initialize_months()
    for x in modelx:
        if isinstance(x['Warranty'], datetime.date):            
            if (model in x['Modelx'] and x['Warranty'].year == 2018):
                for i in range(1,13):
                    if x['Warranty'].month == i:
                        currentmonth = calendar.month_abbr[i]
                        monthcounts[currentmonth] = monthcounts[currentmonth] + 1
    return monthcounts
                        
def add_results(monthtotals, model):
    if 'N' in model:
        make = 'MakeA'
    else:
        make = 'MakeB'    
    new = dict([('Make',make),('Model', model)])
    new.update(monthtotals)
    return new

def calc_prices(price, monthtotalsdict):
    pricedict = initialize_months()
    for i in range(1,13):
        currentmonth = calendar.month_abbr[i]
        pricedict[currentmonth] = monthtotalsdict[currentmonth] * price
        return pricedict

results = []
priceresults = []
prices = read_csv('pricelist.csv')

model1Aand1B = read_csv('model1Aand1B.csv')
fix_dates(model1Aand1B)

for model in ['1A', '1B']:    
    monthtotals = count_dates_for_models(model1Aand1B, model)
    results.append(add_results(monthtotals, model))
    for p in prices:
        if (model in p['Description'] and '1 year' in p['Description']):      
            pricetotals = calc_prices(int(p['net Price']), monthtotals)
            priceresults.append(add_results(pricetotals, model))

model2Aand2B = read_csv('model2Aand2B.csv')
fix_dates(model2Aand2B)

for model in ['2A', '2B']:
    monthtotals = count_dates_for_models(model2Aand2B, model)
    results.append(add_results(monthtotals, model))
    for p in prices:
        if (model in p['Description'] and '1 year' in p['Description']):      
            pricetotals = calc_prices(int(p['net Price']), monthtotals)
            priceresults.append(add_results(pricetotals, model))

model3Aand3B = read_csv('model3Aand3B.csv')
fix_dates(model3Aand3B)

for model in ['3A', '3B']:
    monthtotals = count_dates_for_models(model3Aand3B, model)
    results.append(add_results(monthtotals, model))
    for p in prices:
        if (model in p['Description'] and '1 year' in p['Description']):      
            pricetotals = calc_prices(int(p['net Price']), monthtotals)
            priceresults.append(add_results(pricetotals, model))    

monthabbr = []
for i in range(1,13):
    monthabbr.append(calendar.month_abbr[i])

fieldnames = ['Make','Model'] + monthabbr

with open ('output.csv','wt') as outputf:
    writer = csv.DictWriter(outputf,fieldnames=fieldnames)
    writer.writeheader()
    for r in priceresults:
        writer.writerow(r)
    
