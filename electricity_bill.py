def calculateElectricityBill(units: int) -> float:
    if units < 0:
        return -1.0
    
    bill = 50.00  # Fixed meter surcharge
    
    if units <= 100:
        bill += units * 1.50
    elif units <= 200:
        bill += (100 * 1.50) + (units - 100) * 2.50
    elif units <= 300:
        bill += (100 * 1.50) + (100 * 2.50) + (units - 200) * 4.00
    else:
        bill += (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + (units - 300) * 5.00
        
    return round(bill, 2)