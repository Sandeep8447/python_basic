import random

real_num = random.randrange(10)
for i in range(3):
    guess_num = raw_input("please guess the real num:").strip()
    if len(guess_num) == 0:
        continue
    if guess_num.isdigit():
        guess_num = int(guess_num)
    else:
        print "You need input a integer instead of a string."
        continue
    if guess_num > real_num:
        print "Wrong! you need try smaller!"
    elif guess_num < real_num:
        print "Wrong! you need try bigger!"
    else:
        print "Congratulations! you got it!"
        break
else:
    print "Sorry, you have no chance. The real number is", real_num