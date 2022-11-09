

def bartsimpson():
    #Sets Speech to user input
    speech = input('Talk to Bart Simpson: ')
    #if user says Skateboard, print 'Cowabunga!'
    if speech in ['Skateboard', 'skateboard', 'Skate Board', 'skate board']:
      print('Cowabunga!')
    #if user says Sorry, print "Don't have a cow man!"  
    elif speech in ['Sorry', 'sorry', 'My Apologies', 'my apologies', 'Apologies', 'apologies']:
        print("Don't have a cow man!")
    #If user says something else, print 'Eat my shorts!' 
    else: print('Eat my shorts!')

#Restarts script after input
while True:
    bartsimpson()
    
