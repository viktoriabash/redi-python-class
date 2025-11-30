import pandas as pd

#STEP 1: taking the data from csv file, printing data preview

def main(): # function to read csv file (raw data), calculate basic totals and print the results 
    user_input_path = input("Enter CSV file path (or press Enter for default 'raw_data/events_sample.csv'): ").strip()
    if user_input_path == "":
        file_path = "raw_data/events_sample.csv" #default file path
    else:
        file_path = user_input_path
    print(f"\nSource file for usage: {file_path}")
        
    try: #explanation of try & except block: https://www.geeksforgeeks.org/python/try-except-else-and-finally-in-python/
        data = pd.read_csv("raw_data/events_sample.csv")
    except Exception as error:
        print("Something went wrong while reading the CSV file.")
        print("Error details:", error)
        return

#STEP 2: Input from the terminal what data do we need: filetr by time, user_id, order_id, user_city
    print("\nChoose the filter you want to apply (or press Enter to skip):")
    print("1. date")
    print("2. user_id")
    print("3. order_id")
    input_filter = input("Enter your choice (1/2/3): ").strip()
    
# 2.0 Input filter 0: NO FILTER -> database as it is
    if input_filter == "":
        print("No filter selected.")
        
# 2.1 Input filter 1: DATE RANGE
    elif input_filter == "1":
        start_str = input("Enter START date in format YYYY-MM-DD (or press ENter to skip): ").strip()
        end_str = input("Enter END date in format YYYY-MM-DD (or press ENter to skip): ").strip()
        
        data["event_date"] = pd.to_datetime(data["event_date"], errors="coerce")  #https://docs.vultr.com/python/third-party/pandas/to_datetime  pd.to_datetime() is a pandas function that converts values into datetime objects.
    # START date filter    
        if start_str !="":
           try:
               start_date = pd.to_datetime(start_str)
           except: 
               print("Invalid START date! Run the program again.")
               return
           data = data[data["event_date"] >= start_date]
    # END date filter 
        if end_str != "":
            try:
                end_date = pd.to_datetime(end_str)
            except:
                print("Invalid END date! Run the program again.")
                return
            data = data[data["event_date"] <= end_date]
            
            if data.empty: # checks true/false if empty ://www.geeksforgeeks.org/python/python-pandas-dataframe-empty/
               print("No data found for this date range.")
               return
            else:
                print("\nApplying date filter...")
                print(f"Data filter {start_date} - {end_date} applied.") 
                                  
# 2.2 Input filter 2: USER_ID        
    elif input_filter == "2":
        print("Applying user_id filter")
        filter_user_id = input("\nType here a specific user_id: ").strip()
        
        if filter_user_id != "":
            filtered_user_id = data[data["user_id"] == filter_user_id]
            
            if filtered_user_id.empty: #no rows in the filtered new table
                print(f"\n No rows found for user_id = {filter_user_id}. Run the program again.")
                return
            else:
                print(f"Filtering data for user_id = {filter_user_id}")
                data = filtered_user_id
                
# 2.3 Input filter 3: ORDER_ID                     
    elif input_filter == "3":
        print("Applying order_id filter..")
        filter_order_id = input("\nType here a specific order_id: ").strip()
        if filter_order_id
        
        
    else:
        print("Invalid input, no filter applied.")
        return
        

    
    print("Data preview: ")
    print(data.head()) # to show first 5 rows
    print()
    
    
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
# TO ADD multiple choices, e.g. 1+2??????   
# to add number of views to the file and KPIS   
# to uses classes
# errors checks
# __x__ privacy for some info about users (to add a column with bank card number)      