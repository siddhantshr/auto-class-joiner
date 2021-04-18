import json

def check():
    try:
        with open("data/links.json") as f:
            pass
    except:
        with open("data/links.json","w") as f:
            f.write("")
    try:
        with open("data/classes.json") as f:
            pass
    except:
        with open("data/classes.json","w") as f:
            f.write("")



def view_links():
    with open("data/links.json") as f:
        try:
            dic = json.load(f)
            string = json.dumps(dic, indent=4)[1:-1]
            string = "".join(map(lambda a: "" if a in {'"',','} else a, string))
            print(f"The links stored presently:{string}")
            print("=====================================")
            return dic
        except json.decoder.JSONDecodeError:
            print("Empty!")
            return None
            

def view_timetable():
    with open("data/classes.json") as f:
        try:
            string = json.dumps(json.load(f), indent=4)[1:-1]
            replace = {'"',',', "[", "]","{","}"}
            string = "".join(map(lambda a: " " if a in replace else a, string))
            print(f"The timetable stored presently:{string}")
            print("=====================================")
        except json.decoder.JSONDecodeError:
            print("Empty!")

def add_record():
    days = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"}
    for i in days: print(f"\t{i}")
    while (user:=input("Select day: ").capitalize()) not in days: print("Invalid day!")
    user = user.lower()
    while True:
        timed = input("Enter time in form HH:MM ")
        try:
            hour, minutes = map(int,timed.split(":"))
            if hour>=0 and hour < 24 and minutes >=0 and minutes < 60:
                break
            print("Invalid input!")
        except Exception:
            print("Invalid input!")
    with open("data/classes.json") as f:
        try:
            dictionary = json.load(f)
        except json.decoder.JSONDecodeError:
            dictionary = {}
    if timed in dictionary:
        print("Please edit the record and not add another!")
        return
    subjects =[]
    while input("Enter a subject? (y/n): ").lower() == "y":
        print("Here are the valid subjects and links: ")
        check = view_links()
        if not check:
            print("No links available!")
            print("Please add the subject in links.json first!")
            return
        else:
            while (subject:=input("Enter subject: ")) not in check:
                print("Invalid subject")
                if input("Do you want to return? (y/n): ").lower() == "y":
                    return
            subjects.append(subject)
    try:
        dictionary[user][timed].extend(subjects)
    except:
        dictionary[user][timed] = subjects
    with open("data/classes.json", "w") as f:
        f.write(json.dumps(dictionary, indent = 4))
    

def edit_record():
    with open("data/classes.json") as f:
        try:
            dictionary = json.load(f)
        except json.decoder.JSONDecodeError:
            print("No record found!")
            return
    while (user:=input("Select day: ").lower()) not in dictionary: print("Invalid day!")
    user = user.lower()
    while (timed:=input("Select time: ")) not in dictionary[user]: print("Invalid time!")
    for i in dictionary[user][timed]:
        print(i)
    print("Here are the subjects in the slot.")
    subjects = dictionary[user][timed]
    print("""
1. Add subject
2. Remove subject""")
    while not ((user1:=input("Select option: ")).isdigit() and int(user1) in range(1,3)):
            print("Invalid option")
    if user1 == "1":
        while input("Enter a subject? (y/n): ").lower() == "y":
            print("Here are the valid subjects and links: ")
            check = view_links()
            if not check:
                print("No links available!")
                print("Please add the subject in links.json first!")
                return
            else:
                while (subject:=input("Enter subject: ")) not in check:
                    print("Invalid subject")
                    if input("Do you want to return? (y/n): ").lower() == "y":
                        return
                subjects.append(subject)
        
    else:
        print("Here are the valid subjects:",*subjects, sep ="\n")
        while input("Remove a subject? (y/n): ").lower() == "y" and subjects!=[]:
            while (subject:=input("Enter subject: ")) not in subjects:
                print("Invalid subject")
            subjects.remove(subject)
    if subjects:
        dictionary[user][timed] = subjects
    else:
        del dictionary[user][timed]
    with open("data/classes.json", "w") as f:
        f.write(json.dumps(dictionary, indent = 4))

def remove_all():
    if input("Write confirm and press enter to continue: ")!= "confirm":
        return
    with open("data/classes.json", "w") as f:
            f.write("")

    
def main():
    print("Generating timetable.json!")
    while True:
        print("""
1. View Timetable
2. Add record
3. Edit record
5. Delete all contents
6. Done
              """)
        switch = {"1": view_timetable, "2": add_record, "3": edit_record, "5": remove_all, "6": exit}
        while not ((user:=input("Select option: ")).isdigit() and int(user) in range(1,7)):
            print("Invalid option")
        switch[user]()

check()
main()