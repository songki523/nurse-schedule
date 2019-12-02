import os, datetime
import csv

nurse_name = None
now = datetime.datetime.now()
month = None
dates = None
relative_path = None
file_name = None

print("Nurse Schedule Date Calender")
nurse_name = input("What is your Name?:  ")
print("Hi! {},".format(nurse_name))
month = input("What Month are you entering?(In numbers):  ")
dates = input("What are the dates (Please Enter it in comma separated values. ex.1,2,15,20,25:  ")
relative_path = os.path.expanduser("~/Downloads")
file_name = relative_path + "/{} Day Shift {}-{}-{}.csv".format(nurse_name, month, now.day, now.year)

# Todo: check value
# Loop over dates
_collections = []
dates_list = dates.split(",")
for day in dates_list:
    _collections.append(
        {"Subject": "{} Day Shift".format(nurse_name),
         "Start Date": "{}/{}/{}".format(month, day, now.year)}
    )


# Save it as csv file
def store_into_csv(collections):

    file_exists = os.path.isfile(file_name)

    with open(file_name, 'w') as _csvFile:
        _fieldnames = ['Subject', 'Start Date']
        writer = csv.DictWriter(_csvFile, fieldnames=_fieldnames)

        if not file_exists:
            writer.writeheader()
        writer.writerows(collections)


# Add value
store_into_csv(_collections)
print("Done!")
