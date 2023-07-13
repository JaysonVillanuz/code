#this part will ask the user to input how many days to put
number_of_days = float(input("Enter the  number of days: "))

#given of rate per day
rate_per_day = 15000
#given of sound system fee
sound_system_fee = 4500
#given of stage decor fee
stage_decor_fee = 3000
#given of catering fee
catering_Fee = 35000
#given of evat
evat = .12
#the formula of the bill and the computation

#computaton of amount
amount = rate_per_day * number_of_days
#computation of total amoung by adding amount,sound system and catering fee
total_amount = amount + sound_system_fee + stage_decor_fee + catering_Fee

#tax computation multiply the total amount and evat
tax = total_amount * evat

#computation of bill adding total amount and tax
bill = total_amount + tax

#the final computation and to print the bill
print("Bill = ",bill)