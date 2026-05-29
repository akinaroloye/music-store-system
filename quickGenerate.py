import random
import datetime

recordIDs = [
    "zeom", "cfhg", "nkfl", "keqo", "hfex", "tefp", "oght", "ywru", "jbch", "azdp",
    "aldh", "erqr", "ddgn", "zncy", "tsds", "dice", "tyit", "opdr", "djvh", "wlob"
]

userIDs = [
    "xfge", "diwq", "aptn", "wvoc", "ncxv", "slwj", "fewd", "ytkq", "jmov", "tofg",
    "dszo", "uhck", "jibj", "gvut", "afjw", "tlxv", "ahkp", "ntgp", "obul", "asgw"
]

def random_date(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    return start_date + datetime.timedelta(days=random_days)

start_date = datetime.date(2024, 1, 1)
end_date = datetime.date(2024, 12, 11)

data_lines = ["RecordID,RentalDate,ReturnDate,RentalCustomerID"]

for recordID in recordIDs:
    rental_date = random_date(start_date, end_date)
    if random.choice([True, False]):
        return_date = random_date(rental_date, end_date)
        return_date_str = return_date.strftime("%Y-%m-%d")
    else:
        return_date_str = " "
    rental_customer_id = random.choice(userIDs)
    line = f"{recordID},{rental_date.strftime('%Y-%m-%d')},{return_date_str},{rental_customer_id}"
    data_lines.append(line)

# Print the data
for line in data_lines:
    print(line)
