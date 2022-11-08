


# Sets speech to what user input
speech = input("Talk to Bart Simpson: ")

#If users says skateboard print 'Cowabunga!' else if user apologizes print "Don't have a cow man!" else print 'Eat my shorts!
if speech in ['Skateboard', 'skateboard', 'Skate Board', 'skate board']:
      print('Cowabunga!')
elif speech in ['Sorry', 'sorry', 'My Apologies', 'my apologies', 'Apologies', 'apologies']:
    print("Don't have a cow man!")
else: print('Eat my shorts!')

