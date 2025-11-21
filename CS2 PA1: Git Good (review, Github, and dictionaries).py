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

term_dates = {
    "mod 1" : "August 27 - October 2",
    "mod 2" : "October 6 - November 6 ",
    "mod 3" : "November 10 - December 19",
    "mod 4" : "January 5 - February 6",
    "mod 5" : "February 10 - March 13 ",
    "mod 6" : "March 30 - April 30",
    "mod 7" : "May 4 - June 5",
    "fall" : "August 20 - Oct 31",
    "spring" : "November 3 - February 20",
    "winter" : "February 23 - May 29"

}


#clean_input is a reuseable function that removes white whites space from user input
def clean_input(text):
    return text.strip()


#a which_schedule creates the mod or d block you are putting input into
def which_schedule():
    result = input("Add a schedule: Mod or D Block?\n> ")
    while not clean_input(result) in ["mod", "d block", "d", "m"]:
        print("Error! Please type correct name")#error handling
        result = input("Add a schedule: Mod or D Block?\n> ")
    
    if result in ["mod", "m"]:            
        return "mod"
    else:            
        return "dblock"


#verify_name checks if the name of your mod is valid so you cant say mod 9 (Only if you picked mod)
def verify_name(): #mod
    answer =  input("what mod are you scheduling, enter a number between 1 and 7? \n> ")
    mod_name = "mod " + answer    
    while clean_input(mod_name) not in user_schedule.keys():
        print("error: between 1 and 7")
        answer =  input("what mod are you scheduling, enter a number between 1 and 7? \n> ")
        mod_name = "mod " + answer 
    if any(value != "" for value in user_schedule[mod_name].values()):
            print("Error: This mod already has classes. Pick another mod.")#error handling
    return mod_name




        

# dblock_name and dblock_szn asks for the name of your dblock and season and puts it in the dictionary
def dblock_name(): #dblock
    season = dblock_szn()
    name = input ("what is the name of your d block? \n>")
    user_schedule["dblock"].update({season: name})


def dblock_szn(): 
    szn = input ("what is the season of your dblock\n>" )
    while szn not in user_schedule["dblock"].keys():
        print("error: pick between fall winter and spring \n>")
        szn = input ("what is the season of your dblock\n>")
        if user_schedule["dblock"][szn] != "":
            print("Error: that season already has a D Block class. Pick another season.")
            continue
    return szn 


#add_class adds a block to your mod 
def add_class(mod):
    add = True
    while add:
        block = input("what class do you want to add? a block, b block, or c block \n>")
        if block not in ["a block", "b block", "c block"]: #error handling
            print("error: please say a block, b block or c block \n>")
            continue
        class_name = input("What is the name of your class \n>")
        if user_schedule[mod][block] == "":          
            user_schedule[mod].update({block: class_name})
            print("class added")
        else: 
            print("Error, you cannot add 2 of the same classes in the same mod. TRY AGAIN")
        while True:
            add_new = input("would you like to add a new class? (yes/no)\n>").strip().lower()
            if add_new in ["no"]:
                return        # go back to main()
            if add_new in ["yes", "y"]:
                break         # go add another class
            print("Error: please type yes or no.\n") #error handling
    

def is_schedule_empty(schedule): # checks which keys in the dictionary are empty
    for key, value in schedule.items():
        for mod_name, classes in value.items():
            if classes != "": 
                return False
    return True


def view_schedule(schedule):
    for key, value in schedule.items():
        for mod_name, classes in value.items():
            if classes != "":  
                print(" ") # (" ") added to make view schedule easier to look at
                print(key + " " + term_dates[key]) 
                print(" ")             
                print(mod_name + " " + classes)



    
def main():
    
    running =  True
    add_more = True
    print("Welcome")
    question = "schedule"
    while running:
        if not is_schedule_empty(user_schedule):
            question = input("Would you like to 1. create a schedule 2. view schedule 3. leave program ")

        if question in ["3"]: #if the answer is 3 the program will say goodbye and end
            print("Thank You, Goodbye")
            running = False

        if question in ["view", "v", "2"]: #if the answer is 2 the program will show the view schedule function
            view_schedule(user_schedule)

        if question in ["1", "schedule"]: # if the answer is 1 the program will loop back to adding another schedule         
            option = which_schedule()        
            if option == "mod":
                mod_added = verify_name()
                print("great lets add a class\n")
                add_class(mod_added)
                                    
            elif option == "dblock":
                dblock_name()
                print("d block added")
        
        new_class = input("would you like to add another schedule?\n>")
        if new_class == "no":
            add_more = False
        else:
            option = which_schedule()
                    
           
main()


