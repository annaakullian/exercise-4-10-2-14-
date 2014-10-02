def numbers_list(num, inc):
    i = 0
    numbers = []
    while i < num:
        print "At the top i is %d" % i
        numbers.append(i)
        i = i+inc
        print "numbers now: ", numbers
        print "At the bottom i is %d" %i


def numbers_list_range(num, inc):
    numbers = []
    for i in range(0, num, inc):
        print "At the top i is %d" % i
        numbers.append(i)
        print "numbers now: ", numbers
        print "At the bottom i is %d" % (i+inc)

input = raw_input("Give me a number:")
increment = raw_input("Give me an inc:")
user_number = int(input)
user_inc = int(increment)

numbers_list(user_number, user_inc)
numbers_list_range(user_number, user_inc)
