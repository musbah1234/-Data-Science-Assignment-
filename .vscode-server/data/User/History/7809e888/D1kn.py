from datetime import datetime

# Get current date and time
current_datetime = datetime.now()

# Extract components
current_day = current_datetime.day
current_month = current_datetime.month
current_year = current_datetime.year
current_hour = current_datetime.hour
current_minute = current_datetime.minute
current_timestamp = current_datetime.timestamp()

# Print results
print(f"Current Day: {current_day}")
print(f"Current Month: {current_month}")
print(f"Current Year: {current_year}")
print(f"Current Hour: {current_hour}")
print(f"Current Minute: {current_minute}")
print(f"Timestamp: {current_timestamp}")
   

   
# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

formatted_date = current_datetime.strftime("%m/%d/%Y, %H:%M:%S")
print(f"Formatted Date: {formatted_date}")

time_string = "5 December, 2019"
time_object = datetime.strptime(time_string, "%d %B, %Y")
print(f"Time Object: {time_object.time()}")

