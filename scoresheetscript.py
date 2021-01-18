from tkinter import *

#   #   #   #   #
#   Inst Vars.  #
#   #   #   #   #
endProgram = False
firstRecord = ["Enter Player 1...", "P1 Character", "Stocks Taken", "Enter Player 2...", "P2 Character", "Stocks Taken", "Winner"]
records = [firstRecord]
matches = ["1. " + firstRecord[0] + "(" + firstRecord[1] + ")[" + firstRecord[2] + "] vs. [" + firstRecord[5] + "](" + firstRecord[4] + ")" + firstRecord[3]]
lastTeamWon = 0
offset = "                             \n"
score1 = 0
score2 = 0
crew1 = ""
crew2 = ""

#   #   #   #   #
#   Functions   #
#   #   #   #   #
def createRecord():
    p1 = input("Enter Team 1's Player: ")
    p1Char = input("Enter Team 1's Player's Character: ")
    p2 = input("Enter Team 2's Player: ")
    p2Char = input("Enter Team 2's Player's Character: ")
    p1score = int(input("How many stocks did Team 1's player take: "))
    p2score = int(input("How many stocks did Team 2's player take: "))
    while True:
        winnerIn = input("Who won(Enter 1 or 2): ")
        print(winnerIn)
        if winnerIn == '1':
            winner = 1
            break
        elif winnerIn == '2':
            winner = 2
            break
        else:
            print("Invalid Input")
    newRecord = [p1, p1Char, p1score, p2, p2Char, p2score, winner]
    return newRecord

def resetTextFiles():
    scoreSheetOverlayVs = open('scoreSheetOverlayVs.txt', 'w')
    scoreSheetCrew1 = open('scoreSheetCrew1.txt', 'w')
    scoreSheetCrew2 = open('scoreSheetCrew2.txt', 'w')
    scoreSheet = open('scoreSheet.txt', 'w')

    scoreSheetCrew1.write(offset)

    scoreSheetOverlayVs.close()
    scoreSheetCrew1.close()
    scoreSheetCrew2.close()
    scoreSheet.close()

def writeToScoreSheets(record):
    scoreSheetOverlayVs = open('scoreSheetOverlayVs.txt', 'a')
    scoreSheetCrew1 = open('scoreSheetCrew1.txt', 'a')
    scoreSheetCrew2 = open('scoreSheetCrew2.txt', 'a')
    scoreSheet = open('ScoreSheet.txt', 'a')

    scoreSheetCrew1.write(record[0] + " [" + str(record[2]) + "]\n")
    scoreSheetOverlayVs.write("vs.\n") 
    scoreSheetCrew2.write("[" + str(record[5]) + "] " + record[3] + "\n")

    if record[6] == 1:
        player1Final = "**" + record[0] + "(" + record[1] + ") [" + str(record[2]) + "]**"
        player2Final = record[3] + "(" + record[4] + ") [" + str(record[5]) + "]"
    else:
        player1Final = record[0] + "(" + record[1] + ") [" + str(record[2]) + "]"
        player2Final = "**" + record[3] + "(" + record[4] + ") [" + str(record[5]) + "]**"

    scoreSheet.write(player1Final + " vs. " + player2Final + "\n")

    scoreSheetOverlayVs.close()
    scoreSheetCrew1.close()
    scoreSheetCrew2.close()
    scoreSheet.close()


#   #   #   #   #   
# Tkinter functions
#   #   #   #   #

# New Score Sheet



# Edit

# Finalize


#   #   #   #   #   #
#   Tkinter Window  #
#   #   #   #   #   #

master = Tk()

variable = StringVar(master)
variable.set(matches[0]) # default value

w = OptionMenu(master, variable, *matches)
w.pack()

# New match
def newMatch():
    newRecord = ["Enter Player 1...", "P1 Character", "Stocks Taken", "Enter Player 2...", "P2 Character", "Stocks Taken", "Winner"]
    records.append(newRecord)
    matches.append(str(len(matches)) + ". " + newRecord[0] + "(" + newRecord[1] + ")[" + newRecord[2] + "] vs. [" + newRecord[5] + "](" + newRecord[4] + ")" + newRecord[3])
    print(records)
    w = OptionMenu(master, variable, *matches)
    w.pack() 

p1Var = firstRecord[0]
p1Char = firstRecord[1]
p1Score = firstRecord[2]
p2Var = firstRecord[3]
p2Char = firstRecord[4]
p2Score = firstRecord[5]

p1Entry = Entry(master)
p1Entry.insert(END, p1Var)
p1Entry.pack()

addRecordBtn = Button(master, text="+ Add Match", command=newMatch)
addRecordBtn.pack()


# start the loops
mainloop()

#   #   #   #   #
#   Loop        #
#   #   #   #   #

# while not endProgram:
#     print("Command List:\n- N: New Score Sheet\n- I: Insert new match\n- M: Insert Multiple matches\n- F: Finalize Score Sheet(In progress)\n- E: Edit a Match\n- X: Exit program")
#     cmd = input("Enter command: ")

#     # Insert New Matches
#     if cmd == 'I' or cmd == 'M':
#         matches = 1
#         if(cmd == 'M'):
#             matches = int(input("How many matches to record: "))
        
#         for x in range(matches):
#             record = createRecord()
#             records.append(record)
#             print(records)
#             writeToScoreSheets(record)

#     # Start a new score sheet
#     elif cmd == 'N':
#         resetTextFiles()
#         scoreSheet = open("ScoreSheet.txt", 'w')
#         crew1File = open('crew1.txt', 'w')
#         crew2File = open('crew2.txt', 'w')
#         crew1 = input("Enter name of first crew: ")
#         crew2 = input("Enter name of second crew: ")
#         crew1File.write(crew1)
#         crew2File.write(crew2)
#         scoreSheet.write("__**@" + crew1 + " vs. @" + crew2 + "**__\n")
#         crew1File.close()
#         crew2File.close()

#     # Finalize Score Sheet
#     elif cmd == 'F':
#         winningCrew = input("Winning Crew Name: ")
#         score1 = int(input("Score 1: "))
#         score2 = int(input("Score 2: "))
#         scoreSheet = open("ScoreSheet.txt", 'a')
#         scoreSheet.write("**" + winningCrew + " wins " + str(score1) + "-" + str(score2) + "**")
#         scoreSheet.close()

#     elif cmd == 'E':
#         print("Which record to edit?")
#         for i in range(len(records)):
#             match = records[i]
#             print(str(i) + ". " + match[0] + " [" + str(match[2]) + "] vs. [" + str(match[5]) + "] " + match[3] + " - Winner is Crew: " + str(match[6]))
#         userIn = -1
#         while userIn < 0 or userIn > len(records):
#             userIn = int(input("Enter record number: "))

#         records[userIn] = createRecord()
#         resetTextFiles()
#         scoreSheet = open("ScoreSheet.txt", 'a')
#         scoreSheet.write("__**@" + crew1 + " vs. @" + crew2 + "**__\n")
#         scoreSheet.close()
#         for j in range(len(records)):
#             writeToScoreSheets(records[j])

#     elif cmd == 'X':
#         endProgram = True
    
#     else:
#         print("Invalid command")

    