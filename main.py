# Code about no. of days left in the specific date


# Importing date from Datetime module
from datetime import date

# Storing today's date into a variable
today = date.today()

# Storing the specific date
graduation_day = date(2023, 8, 11)

# finding the difference of today's date from
# specified date
days_left = abs(graduation_day - today)

# day_left == minus value or todays

# Displaying the no.of.days left without time
print(f"Number of days left till graduation: {days_left}")

 # def ran_gen(size, chars=string.ascii_uppercase + string.digits):
    #     return ''.join(random.choice(chars) for x in range(size))
    # item6 = ran_gen(8, "ABCD1234")
    # print ("Your User ID is:" , item6)


# Assign unique value to list elements
# dict_ids = list(map({}.setdefault, Alist, count()))
