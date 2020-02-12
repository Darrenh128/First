def hotel_cost():
    print("how many nights do you want to stay: ")
    nights = int(input())
    per_night_rate = 100
    return per_night_rate * nights



def plane_ride_cost():
    print("Where do you want to go: ")
    city = str(input())
    if city =='charlotte':
        return 183
    elif city =='tampa':
        return 220
    elif city =='pittsburg':
        return 222
    elif city =='los angles':
        return 475

 # print "section" and 'city' and that will return a ticket price

# if you want to increment the tickets by 10 (or any number)



def car_rental_cost():
    print("How many days do you want to rent a vehicle for?: ")
    days = int(input())
    day_rate = 40
    return days * day_rate


'''    if days >= 7:               # if renting for 7 days or more you minus 50 from the total bill
        total_cost = total_cost -50
        return total_cost
    elif days >= 3:             # if renting for 3 days or more you minus 20 from the total bill
        total_cost = total_cost -20
        return total_cost
'''


#Total_holiday_cost = plane_ride_cost(),+ car_rental_cost(),+ hotel_cost()

answer = plane_ride_cost()+car_rental_cost()+hotel_cost()


print(hotel_cost(), '+' ,plane_ride_cost(), '+' ,car_rental_cost(), '=' ,answer,)
