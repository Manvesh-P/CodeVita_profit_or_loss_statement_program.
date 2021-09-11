brokerage_m = input("Enter the brokerage rate in %: ")
buying_amount_m = input("Enter the buying amount: ")
selling_amount_m = input("Enter the selling amount: ")
quantity_m = input("Enter the quantity of shares: ")

if selling_amount_m == '@':
    print("Invalid Input")
    
else:

    brokerage = float(brokerage_m)
    buying_amount = float(buying_amount_m)
    selling_amount = float(selling_amount_m)
    quantity = int(quantity_m)


    b_price = buying_amount * quantity
    s_price = selling_amount * quantity
    e_profit = s_price - b_price

    brokerage1 = (brokerage / 100) * b_price
    service_tax1 = (10.36 / 100) * brokerage1

    addl_ch1 = brokerage1 + service_tax1

    brokerage2 = (brokerage / 100) * s_price
    service_tax2 = (10.36 / 100) * brokerage2
    stt = (0.025 / 100) * s_price

    addl_ch2 = brokerage2 + service_tax2 + stt

    addl_ch3 = (0.006 / 100) * (b_price + s_price)

    taddl_ch = addl_ch1 + addl_ch2 + addl_ch3

    if e_profit > taddl_ch:
        
        fate = e_profit - taddl_ch
        print("PROFIT")
        print(round(fate,2))

    elif taddl_ch > e_profit:
        
        fate = taddl_ch - e_profit
        print("LOSS")
        print(round(abs(fate),2))

    else:
        
        print("NO LOSS NO PROFIT")
