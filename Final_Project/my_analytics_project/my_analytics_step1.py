import pandas as pd

#Step 1: taking the data from csv file, printing data preview

def main(): # function to read csv file (raw data), calculate basic totals and print the results 
    user_input_path = input("Enter CSV file path (or press Enter for default 'raw_data/events_sample.csv'): ").strip()
    if user_input_path == "":
        file_path = "raw_data/events_sample.csv" #default file path
    else:
        file_path = user_input_path
    print(f"\nSource file for usage: {file_path}")
        
    try:
        data = pd.read_csv("raw_data/events_sample.csv")
    except Exception as error:
        print("Something went wrong while reading the CSV file.")
        print("Error details:", error)
        return
    
    print("Data preview: ")
    print(data.head()) # to show first 5 rows
    print()

#Step 2: choose from the terminal what data do wee need: filetr by time, user_id, order_id, user_city
    print("\nChoose the filter you want to apply (or press Enter to skip):")
    print("1. date")
    print("2. user_id")
    print("3. order_id")
    input_filter = input("Enter your choice (1/2/3): ").strip()
    
    if input_filter == "":
        print("No filter selected.")
    elif input_filter == "1":
        print("/nApplying date filter...")
        # TO ADD
    elif input_filter == "2":
        print("Applying user_id filter")
        filter_user_id = input("\nType here a specific user_id: ").strip()
        
        if filter_user_id != "":
            filtered_user_id = data[data["user_id"] == filter_user_id]
            
            if filtered_user_id.empty: #no rows in the filtered new table
                print(f"\n No rows found for user_id = {filter_user_id}. Run the program again")
                return
            else:
                print(f"Filtering data for user_id = {filter_user_id}")
                data = filtered_user_id
        
    elif input_filter == "3":
        print("Applying order_id filter..")
        # TO ADD
    else:
        print("Invalid input, no filter applied.")
        return
        # TO ADD multiple choices, e.g. 1+2??????    
    
    
#Step 3: Calculating totals for KPIs
    total_sessions = data["session_id"].nunique() #to calc. number of total unique sessions
    total_users = data["user_id"].nunique()
    orders_only = data[data["order_id"].notna()] # create a table with lines incl.only orders
    total_orders = orders_only["order_id"].nunique()

    total_revenue = orders_only["order_value"].sum()

    print("\n=== Summary ===")
    print("Total sessions:", total_sessions)
    print("Total users:   ", total_users)
    print("Total orders:  ", total_orders)
    print("Total revenue: ", round(total_revenue, 2))
    
    print("\n=== Basic KPIs ===")
    if total_sessions > 0:
        conversion_rate = total_orders/total_sessions
    else:
        conversion_rate = 0
    print("Conversion rate: ",round(conversion_rate,2)*100,"%")
    

main()
            
            
# NEXT: 
# to add number of views to the file and KPIS   
# to uses classes
# errors checks
# __x__ privacy for some info about users (to add a column with bank card number)      