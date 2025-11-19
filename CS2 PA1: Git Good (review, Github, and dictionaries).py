user_schedule = {
    "mod 1" : {
        "a block" : "",
        "b block" : "",
        "c block" : "",
          },
    "mod 2" : {
        "a block" : "",
        "b block" : "",
        "c block" : "",
          },
    "mod 3" : {
        "a block" : "",
        "b block" : "",
        "c block" : "",
          },
    "mod 4" : {
        "a block" : "",
        "b block" : "",
        "c block" : "",
          },
    "mod 5" : {
        "a block" : "",
        "b block" : "",
        "c block" : "",
          },
    "mod 6" : {
        "a block" : "",
        "b block" : "",
        "c block" : "",
          },
    "mod 7" : {
        "a block" : "",
        "b block" : "",
        "c block" : "",
          },
    "dblock" : {
        "fall" : "",
        "spring" : "",
        "winter" : "",
          }
}

def which_schedule():
    result = input("Add a schedule: Mod or D Block?\n> ")
    if not result.strip(" ") in ["mod", "dblock", "d", "m"]:
        print("Error! Please type correct name")
        return False
    else:
        if result in ["mod", "m"]:            
            return "mod"
        else:            
            return "dblock"
    
def verify_name(): #mod
   
    answer =  input("what mod are you scheduling, enter a number between 1 and 7? \n> ")
    mod_name = "mod " + answer    
    while mod_name.strip() not in user_schedule.keys():
        print("error: between 1 and 7")
        answer =  input("what mod are you scheduling, enter a number between 1 and 7? \n> ")
        mod_name = "mod " + answer 
    return True

def dblock_name(): #dblock
    name = input ("what is the name of your d block? \n>")
    user_schedule["dblock"].update({name})

def dblock_szn(): 
    szn = input ("what is the season of your dblock\n>" )
    while szn not in user_schedule["dblock"].keys():
        print("error: pick between fall winter and spring")
        szn = input ("what is the season of your dblock\n>")
        answered = "dblock" + szn 
    return True

def add_class():
    block = input("what class do you want to add? a, b, or c ")
    if block not in ["a", "b", "c"]:
        print("error: please say a, b or c")
        return

    # now check the modules
    for mod in ["mod 1", "mod 2", "mod 3", "mod 4", "mod 5", "mod 6", "mod 7"]:
        if f"{block} block" in user_schedule[mod].keys():
            input("What is the name of your class")
            return
    
def main():
    print("Welcome")
    option = which_schedule()  
    
    if option == False:
        return  
    
    elif option == "mod": 
       if not verify_name():
            print("please try again")
            return 
       else:
            print("great lets add a class\n")
            add_class()
            
    elif option == "dblock":
        if not dblock_szn():
            print("please say spring winter or fall")
            return
        elif not dblock_name():
            print("d block added")
    
    # ask for a class
    # ask which block
    # put it in


# main program     
main()

    