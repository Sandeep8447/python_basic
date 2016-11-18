password = 'test'
logout_flag = False
for i in range(3):
    user_input = raw_input("please input you password:").strip()
    if len(user_input) == 0:
        continue
    if user_input == password:
        while True:
            print "welcome back!"
            user_choice = raw_input('''
              1. run a cmd
              2. send a file
              3. exit this level
              4. exit the whole system
            ''').strip()
            user_choice = int(user_choice)
            if user_choice == 1:
                print "going to run a cmd."
            if user_choice == 2:
                print "going to send a file."
            if user_choice == 3:
                print "going to exit"
                break
            if user_choice == 4:
                logout_flag = True
                break
    if logout_flag:
        print "going to logout..."
        break