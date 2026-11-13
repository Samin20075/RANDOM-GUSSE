expence=[
    {"Date":"13-11-2026", "Category":"Food", "Amount":10000},
    {"Date":"13-11-2026", "Category":"Travel", "Amount":1500},
    {"Date":"13-11-2026", "Category":"Clothe", "Amount":5000},
    {"Date":"13-11-2026", "Category":"GYM", "Amount":2000},
    {"Date":"13-11-2026", "Category":"CAR", "Amount":3000},
    {"Date":"13-11-2026", "Category":"Electercity bill", "Amount":4500},
    {"Date":"13-11-2026", "Category":"Food", "Amount":8000},
    
    
]
totalamount=0

for e in expence:
    totalamount=totalamount+e["Amount"]
    
print(totalamount)
category_total = {}

for e in expence:
    cat = e["Category"]
    amount = e["Amount"]

    if cat in category_total:
        category_total[cat] =category_total[cat]+amount
    else:
        category_total[cat] =amount

print(category_total)
for cat, amt in category_total.items():
    print(cat,amt)
    