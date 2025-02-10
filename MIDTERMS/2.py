date=input("Enter the date (mm/dd/yyyy): ")
month_dict = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}
month=date[0:2]
day=date[3:5]
year=date[6:]

formatted_date=month_dict[month]+ " " +str(int(day))+", " +year
print("Date Output: " + formatted_date)
