import webbrowser, datetime, json, time

def read_data() -> dict:
    try:
        with open("data/classes.json") as file:
            data = json.load(file)
        return data
    except:
        print("classes.json not found in data folder!\nPlease ensure that __main__ is in the correct directory")
        exit(1)

def get_day() -> str:
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day = days[datetime.datetime.today().weekday()]
    return day


def get_time_difference(input_time:str) -> int:
    hours, minutes, seconds = time.localtime()[3:6]
    current_time = hours*3600 + minutes*60 + seconds
    hours, minutes = map(int,input_time.split(":"))
    difference = (3600*hours + 60*minutes) - current_time 
    return difference, input_time

def get_links():
    try:
        with open("data/links.json") as f:
            return {i.lower():j for i,j in json.load(f).items()}
    except:
        print("links.json not found in data folder!\nPlease ensure that __main__ is in the correct directory")
        exit(1)

def remove(data, key):
    del data[key]
    if data == {}:
        print("No more classes scheduled for today!\n\n")
        exit(0)

def main():
    data = read_data()[get_day().lower()]
    links = get_links()
    while True:
        while (wait:=min(map(get_time_difference, data)))[0] < 0:
            print(", ".join(data[wait[1]]),f"scheduled at {wait[1]} completed!\n")
            remove(data, wait[1])
        time.sleep(wait[0])
        for subject in data[wait[1]]:
            try:
                if links[subject.lower()] != "":
                    print(f"Opening class {subject}")
                    webbrowser.open(links[subject.lower()])
                    continue
            except KeyError:
                ...
            print(f"Error, could not join class. Subject {subject} not available in links!")
            remove(data, wait[1])

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
-------------------------------------------------""")
main()
                
                
            
            
    
            
            
        
    