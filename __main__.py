import webbrowser, datetime, json, os

def open_link(url: str):
    try:
        if url[0:8] != "https://":
            url = f"https://{url}"
    except IndexError:
        exit(f"{url} is not a valid URL")
    webbrowser.open(url)
    
def check_current_time(now, hours: str, minutes: str):
    return str(now.strftime("%H")) == hours and str(now.strftime("%M")) == minutes

dir_path = os.path.dirname(os.path.realpath(__file__))
try:
    with open(dir_path + "/data/classes.json", 'r') as f, open(dir_path + "/data/links.json", 'r') as f2:
        classes = json.load(f)
        links = json.load(f2)
except FileNotFoundError:
    exit("Could not find the data files")

def getCurrentDay():
    return datetime.datetime.now().strftime("%A")

def getCurrentClass(idx: int):
    try:
        return classes[getCurrentDay().lower()][idx]
    except IndexError:
        print("E")
        exit("Could not find the current scheduled class")

def open_class(idx: int):
    cc = getCurrentClass(idx)
    if cc == "":
        exit("Could not find the current scheduled class")
    open_link(links[cc])

def main():
    done_jobs = [None, None, None, None, None]
    while 1:
        if all(x != None for x in done_jobs):
            exit("Exiting, all classes done")
        if check_current_time(datetime.datetime.now(), "08", "30"):
            if done_jobs[0] is None:
                print("Opening class 1")
                open_class(0)
                done_jobs[0] = "Done"
        if check_current_time(datetime.datetime.now(), "09", "20"):
            if done_jobs[1] is None:
                print("Opening class 2")
                open_class(1)
                done_jobs[1] = "Done"
        if check_current_time(datetime.datetime.now(), "10", "20"):
            if done_jobs[2] is None:
                print("Opening class 3")
                open_class(2)
                done_jobs[2] = "Done"
        if check_current_time(datetime.datetime.now(), "11", "10"):
            if done_jobs[3] is None:
                print("Opening class 4")
                open_class(3)
                done_jobs[3] = "Done"
        if check_current_time(datetime.datetime.now(), "12", "00"):
            if done_jobs[4] is None:
                print("Opening class 5")
                open_class(4)
                done_jobs[4] = "Done"

if __name__ == '__main__':
    print(r"""
    _         _           ____ _               
   / \  _   _| |_ ___    / ___| | __ _ ___ ___ 
  / _ \| | | | __/ _ \  | |   | |/ _` / __/ __|
 / ___ \ |_| | || (_) | | |___| | (_| \__ \__ \
/_/   \_\__,_|\__\___/   \____|_|\__,_|___/___/
                                               
     _       _                 _ 
    | | ___ (_)_ __   ___ _ __| |
 _  | |/ _ \| | '_ \ / _ \ '__| |
| |_| | (_) | | | | |  __/ |  |_|
 \___/ \___/|_|_| |_|\___|_|  (_)

-------------------------------------------------
<-- AHiddenDonut - https://github.com/AHiddenDonut
Copyright (c) 2021 AHiddenDonut

Running successfully -- No Errors!
""")
    main()