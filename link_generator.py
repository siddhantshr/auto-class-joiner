import json

def check():
    try:
        with open("data/links.json") as f:
            pass
    except:
        with open("data/links.json","w") as f:
            f.write("")

def view_links():
    with open("data/links.json") as f:
        try:
            string = json.dumps(json.load(f), indent=4)[1:-1]
            string = "".join(map(lambda a: "" if a in {'"',','} else a, string))
            print(f"The links stored presently:{string}")
            print("=====================================")
        except json.decoder.JSONDecodeError:
            print("Empty!")
    
def add_link():
    with open("data/links.json") as f:
        try:
            dictionary = json.load(f)
        except json.decoder.JSONDecodeError:
            dictionary = {}
    print("Here are the existing links:")
    view_links()
    user = input("Enter subject name you want to add or press enter to skip: ")
    if user == "":
        return
    else:
        dictionary[user] = input("Enter subject link: ")
        with open("data/links.json", "w") as f:
            f.write(json.dumps(dictionary, indent = 4))
    print("Added subject")
    
def edit_link():
    with open("data/links.json") as f:
        try:
            dictionary = json.load(f)
        except json.decoder.JSONDecodeError:
            print("No links available!")
            return
    print("Here are the existing links:")
    view_links()
    while (user:=input("Enter subject name you want to edit or press enter to skip: ")) not in dictionary and user != "":
        print(f"Subject {user} not found!")
    if user == "":
        return
    else:
        dictionary[user] = input("Enter subject link: ")
        with open("data/links.json", "w") as f:
            f.write(str(json.dumps(dictionary, indent=4)))
    print("Edited subject")
        
def remove_subject():
    with open("data/links.json") as f:
        try:
            dictionary = json.load(f)
        except json.decoder.JSONDecodeError:
            print("No links found!")
            return
    print("Here are the existing links:")
    view_links()
    while (user:=input("Enter subject name you want to delete or press enter to skip: ")) not in dictionary or user != "":
        print(f"Subject {user} not found!")
    if user == "":
        return
    else:
        del dictionary[user]
        with open("data/links.json", "w") as f:
            f.write(json.dumps(dictionary, indent = 4))
    print("Deleted subject")

def remove_all():
    if input("Write confirm and press enter to continue: ")!= "confirm":
        return
    with open("data/links.json", "w") as f:
            f.write("")

    
def main():
    print("Generating links.json!")
    while True:
        print("""
1. View Subjects and links
2. Add subject and link
3. Edit link of a subject
4. Remove subject
5. Delete all contents
6. Done
              """)
        switch = {"1": view_links, "2": add_link, "3": edit_link, "4": remove_subject, "5": remove_all, "6": exit}
        while not ((user:=input("Select option: ")).isdigit() and int(user) in range(1,7)):
            print("Invalid option")
        switch[user]()

check()
main()