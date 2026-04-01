import json
from datetime import date


habits = {
}


def show_menu():
    print("\nHabit Tracker")
    print("1. Add Habit")
    print("2. Mark Habit Complete")
    print("3. View Progress")
    print("4. Exit")


def add_habit():
    habit = input("Enter habit to track")
    habits[habit] = []
    print("Habit added!")

def complete_habit():
    habit_to_mark = input("Which habit did you complete?")
    if habit_to_mark in habits:
        today = str(date.today())
        habits[habit_to_mark].append(today)
        print("Habit logged")

def show_progress():
    for habit, days in habits.items():
        print(habit, ": ", len(days), "days completed")
    

while True: 
    show_menu()
    choice = int(input("Choose action: "))
    if choice == 1: 
        add_habit()
    elif choice == 2:
        complete_habit()
    elif choice == 3: 
        show_progress()
    elif choice == 4: 
        print("Till next time!")
        break



