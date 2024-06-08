import sqlite3
import inquirer
#line 37 and sequese must be in serise always:
from colorama import Fore, Style, init

init(autoreset=True)

conn  = sqlite3.connect('ytmanager.db')
cursor = conn.cursor();

cursor.execute('''
CREATE TABLE IF NOT EXISTS videos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    time INTERGER NOT NULL
)
''')


def list_video():
    cursor.execute("SELECT * FROM videos")
    videos = cursor.fetchall()
    if videos:
        for vid in videos:
            print(vid)
    
def add_video():
    title = input('Enter the title : ')
    time  = input("Enter the Time : ")
    cursor.execute('''
                INSERT INTO videos(title,time) VALUES (?,?)
                 ''',(title,time))
    conn.commit()
    print("Added")
def update_video():
    list_video()
    # again adding list to point is fun
    index = input("Enter the index you want to update : ")
    title = input('Enter the title : ')
    time  = input("Enter the Time : ")
    cursor.execute('''
                UPDATE videos SET title = ?,time = ?, WHERE id = ?
                 ''',(title,time,index))
    conn.commit()

    pass
def remove_video():
    list_video()
    index = input("Enter the index you want to update : ")
    cursor.execute('''
                DELETE FROM videos WHERE id = ?
                 ''',(index,))
    conn.commit()
    pass


def main():
    while True:
        print( Style.BRIGHT + 'Youtube manager  | choose a option')
        # print(Fore.CYAN + '1. List vid')
        # print(Fore.GREEN + '2. Add vid')
        # print(Fore.RED + '3. Update vid')
        # print(Fore.MAGENTA +'4. Delete vid')
        # print(Fore.YELLOW +'5. Exit')
        question = [
            inquirer.List(
                'option',
                message = 'Select a action',
                choices = [
                    'List Video',
                    'Add Video',
                    'Update Video',
                    'Remove Video',
                    'Exit'
                ],
            ),
        ]

        answer = inquirer.prompt(question)
        option = answer['option']

        match option:
            case 'List Video':
                list_video()
            case 'Add Video':
                add_video()
            case 'Update Video':
                update_video()
            case 'Remove Video':
                remove_video()
            case "Exit":
                break
            case _:
                print(Fore.RED + "Invalid choose")

     

if __name__ == '__main__':
    main()

conn.close()