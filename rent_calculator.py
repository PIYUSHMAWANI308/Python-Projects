## input we need from user
# Total rent
# Total of food
# Electricity unit spend
# charge per unit
# person living in room/flar

## output 
# Total amount you've to pay

rent = int(input("Enter your flat/room rent : "))
food = int(input("Enter your total amount spend for food : "))
electricity_spend = int(input("Enter total Electricity spend : "))
charge_unit = int(input("Enter charge per unit : "))
person = int(input("Enter number of people living in room/flat : "))

electricity = electricity_spend * charge_unit

total = (rent + food + electricity) / person

print(f"You have to pay {total} rupeey in this month")