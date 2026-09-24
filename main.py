import json
import datetime
import csv


# with open("expenses.csv","w",newline= " ") as file:
#     writer = csv.writer(file)
#     writer.writerow(["Expense", "Amount", "Category", "Date"])
#     for item in Data_list:
#         writer.writerow([
#             item["expense"],
#             item["amount"],
#             item["category"],
#             item[datetime]
#         ])



Data_list = []


def add_expense():
    expense = input("Enter Your Expense: ")
    amount = float(input("Enter Your Expense Amount: "))
    category = input("Enter expense Category: ")
    # print(f"Date & Time: {item.get("datetime", "No Date")}")
    current_datetime = datetime.datetime.now()
    current_datetime = current_datetime.strftime("%d-%m-%Y %I:%M %p")
    data = {
    "expense": expense,
    "amount": amount,
    "category": category,
    "datetime": current_datetime
    }

    Data_list.append(data)
    save_expense_data()
    print("Expense Added Successfully!")


def view_expense():
    if len(Data_list) == 0:
        print("No Expense Found")
    else:
        for item in Data_list:
            print(f"Expense Name: {item['expense']}")
            print(f"Amount: ₹{item['amount']}")
            # print(f"Categroy {item['category']}")
            # print(item.get("category", "No Category"))
            print(f"Category: {item.get('category', 'No Category')}")
            print(f"Date & Time: {item.get('datetime', 'No Date')}")
            print("----------------------")


def show_total():
    total = 0

    for item in Data_list:
        total += item["amount"]

    print(f"Total Expense = ₹{total}")


def delete_expense():
    if len(Data_list) == 0:
        print("No Expense Found")
        return

    print("\nExpenses:\n")

    for index, item in enumerate(Data_list):
        print(f"{index + 1}. {item['expense']} - ₹{item['amount']}")

    ask_user = int(input("\nEnter Expense Number To Delete: "))

    if ask_user > 0 and ask_user <= len(Data_list):
        actual_index = ask_user - 1
        deleted_item = Data_list.pop(actual_index)

        save_expense_data()

        print(f"{deleted_item['expense']} Deleted Successfully!")
    else:
        print("Enter a Valid Expense Number.")


def save_expense_data():
    with open("expenses.json", "w") as f:
        json.dump(Data_list, f, indent=4)


def load_expense_data():
    global Data_list

    try:
        with open("expenses.json", "r") as f:
            Data_list = json.load(f)

    except FileNotFoundError:
        Data_list = []

    except json.JSONDecodeError:
        Data_list = []


    

# Load saved data before menu starts
load_expense_data()

def edit_expense():
     if len(Data_list) == 0:
        print("No Expense Found")
        return
     for index, item in enumerate(Data_list):
        print(f"{index + 1}. {item['expense']} - ₹{item['amount']}")

     ask_user = int(input("\nEnter Expense Number To Edit: "))
    
     if ask_user > 0 and ask_user <= len(Data_list):
        actual_index = ask_user - 1
        edit_item = Data_list[actual_index]

        new_name = input("Enter New Expense Name: ")
        new_amount = float(input("Enter New Expense Amount: "))

        edit_item["expense"] = new_name
        edit_item["amount"] = new_amount
        save_expense_data()
        print("Expense Updated Successfully!")
     else:
         print("Enter a valid Expense Number: ")


def search_expense():
    if len(Data_list) == 0:
        print("No Expense Found")
        return
    search = input("Enter Expense Name To Search: ")
    found = False
    for item in Data_list:
        if search in item["expense"]:
           print(f"Expense Name: {item['expense']}")
           print(f"Amount: ₹{item['amount']}")
           print("----------------------")
           found = True
    if found == False:
        print("Search item not found: ")




def category_show():
    total = 0
    category = input("Enter category to show total: ")
    for item in Data_list:
        if item['category'] == category:
            total = total + item['amount']
    print(f"{category} Total: ₹{total}")


def high_expense():
    if len(Data_list) == 0:
        print("No Expense Found")
        return

    Highest = Data_list[0]

    for item in Data_list:
        if item['amount'] > Highest['amount']:
            Highest = item
    print("Highest Expense ")
    print("=========================")
    print(f"Expense: {Highest['expense']}")
    print(f"Amount: ₹{Highest['amount']}")
    print(f"Category: {Highest['category']}")
    # print(f"Category: {Highest.get("category", "No Category")}")
    print(f"Category: {Highest.get('category', 'No Category')}")
    print("==========================")




def lowest_expense():
    if len(Data_list) == 0:
        print("No Expense Found")
        return

    Lowest = Data_list[0]

    for item in Data_list:
        if item['amount'] < Lowest['amount']:
            Lowest = item
    print("Lowest Expense ")
    print("=========================")
    print(f"Expense: {Lowest['expense']}")
    print(f"Amount: ₹{Lowest['amount']}")
    print(f"Category: {Lowest['category']}")
    # print(f"Category: {Lowest.get("category", "No Category")}")
    print(f"Category: {Lowest.get('category', 'No Category')}")
    print("==========================")


def monthly_report():
    if len(Data_list) == 0:
        print("No Expense Found")
        return

    user = input("Enter month (01-12): ")
    report = {}

    for item in Data_list:
        if "datetime" not in item:
            continue
        parts = item["datetime"].split("-")
        month = parts[1]

        if user == month:
            category = item["category"]
            amount = item["amount"]

            if category in report:
                report[category] += amount
            else:
                report[category] = amount

    print("\n===== Monthly Report =====")

    for category, amount in report.items():
        print(f"{category} : ₹{amount}")

    print("==========================")



def top_spending_category():
    if len(Data_list) == 0:
        print("No Expense Found")
        return

    report = {}

    # Category wise total
    for item in Data_list:
        category = item["category"]
        amount = item["amount"]

        if category in report:
            report[category] += amount
        else:
            report[category] = amount

    # Highest category find
    highest_category = None
    highest_amount = 0

    for category, amount in report.items():
        if amount > highest_amount:
            highest_amount = amount
            highest_category = category

    print("\n===== Top Spending Category =====")
    print(f"Category : {highest_category}")
    print(f"Amount   : ₹{highest_amount}")
    print("================================")




def average_expense():
    if len(Data_list) == 0:
        print("No Expense Found")
        return
    number_of_transactions = len(Data_list)
    total= 0
    for item in Data_list:
        total = total + item['amount']
    print(f"Total Expense = ₹{total}")

    average = total / number_of_transactions
    print("===== Average Expense =====")
    print(f"Total Expense        : ₹{total}")
    print(f"Transactions         : {number_of_transactions}")
    print(f"Average Expense      : {average}")
    print("==========================")



def expense_between_date():
    total = 0
    if len(Data_list) == 0:
        print("No expense found ")
        return
    
    start_date = input("Enter Start Date (DD-MM-YYYY): ")
    end_date = input("Enter End Date (DD-MM-YYYY): ")
    found = False
    for item in Data_list:
        parts = item["datetime"].split(" ")
        date = parts[0]
        if start_date<= date <= end_date:
            total+=item["amount"]
            found = True
            print(f"Expense Name: {item['expense']}")
            print(f"Amount: ₹{item['amount']}")
            print(f"Category: {item['category']}")
            print(f"Date: {date}")
            print("---------------------------")
    if found == False:
        print("No Specific date found ")
    
    print(f"Total Expense : ₹{total}")



def category_percentage():
    if len(Data_list) == 0:
        print("No expense found ")
        return
    report = {}
    total = 0
    for item in Data_list:
        category = item['category']
        amount = item['amount']
        total+=amount
        if category in report:
            report[category]+= amount
        else:
            report[category] = amount
    # percentage = (amount / total) * 100
    
    for category, amount in report.items():
        print("\n===== Category Percentage =====")
        print(f"Category      : {category}")
        print(f"Amount        : ₹{amount}")
        percentage = (amount / total) * 100
        print(f"Percentage    : {percentage:.2f}%")
        print("----------------------------")
        print("============================")



def budget_status():
    total = 0
    for item in Data_list:
        total+=item["amount"]
    
    budget = int(input("Enter monthly budget: "))
    # remaining = budget - total
    print("===== Budget Status =====")
    print(f"Budget       : {budget}")
    print(f"Spent        :₹{total}")
    # print(f"Remaining    :{remaining}")

    # budget = int(input("Enter monthly budget: "))
    if total<=budget:
        print(" ✅  You are within your budget.")
        remaining = budget - total
        print(f"Remaining    : ₹{remaining}")
        
    else:
        over_budget = total - budget
        print(f"Over Budget  : ₹{over_budget}")
        print(" ⚠️  Warning! Budget Exceeded.")
    print("=========================")



def export_to_csv():
    if len(Data_list) == 0:
        print("No Expense Found")
        return
    # filename = input("Enter CSV file name (without .csv): ")
    with open("expenses.csv", "w", newline="") as file:
    # with open(filename + ".csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Expense", "Amount", "Category", "Date"])

        for item in Data_list:
            writer.writerow([
                item["expense"],
                item["amount"],
                item["category"],
                # item["datetime"]
                item.get("datetime", "No Date")
            ])
    print("Expenses exported successfully!")




while True:
    print("""
========= Expense Tracker =========

1. Add Expense
2. View Expenses
3. Show Total
4. Exit
5. Delete Expense
6. Edit Expense
7. Search Expense
8. Category_show
9. Highest Expense
10. Lowest Expense
11. Monthly Report
12. Top_Spending_Category
13. Average Expense
14. Expense Between Date
15. Category Percentage
16. Budget Status
17. Export Into CSV
===================================
""")

    try:
        user_demand = int(input("Enter your choice: "))

        if user_demand == 1:
            add_expense()

        elif user_demand == 2:
            view_expense()

        elif user_demand == 3:
            show_total()

        elif user_demand == 4:
            print("Good Bye!")
            break

        elif user_demand == 5:
            delete_expense()
        elif user_demand == 6:
            edit_expense()
        elif user_demand == 7:
            search_expense()
        elif user_demand == 8:
            category_show()
        elif user_demand == 9:
            high_expense()
        elif user_demand == 10:
            lowest_expense()
        elif user_demand == 11:
            monthly_report()
        elif user_demand == 12:
            top_spending_category()
        elif user_demand == 13:
            average_expense()
        elif user_demand == 14:
            expense_between_date()
        elif user_demand == 15:
             category_percentage()
        elif user_demand == 16:
            budget_status()
        elif user_demand == 17:
            export_to_csv()
        else:
            print("Enter a valid number.")

    except ValueError:
        print("Please enter numbers only.")


    # GitHub commit test