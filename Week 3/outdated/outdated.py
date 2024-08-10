months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Function to call get_date and convert to correct format

def main():
    x = get_date()
    print(x)

# Function to prompt user for input and check format is correct(mm/dd/yyyy or September 8, 1963)

def get_date():
    while True:
        i = input('Date: ').strip()
        try:
            if i.index(','):
                m,d,y = i.replace(',','').split(' ')
                if m in months:
                    m = months.index(m) + 1
                    if d.isdigit() == True and int(d) >= 1 and int(d) <= 31:
                        if y.isdigit() == True and int(y) >= 1 and len(y) == 4:
                            return (f'{int(y):04}-{int(m):02}-{int(d):02}')
        except(ValueError, KeyError):
            try:
                m,d,y = i.split('/')
                if m.isdigit() == True and int(m) >= 1 and int(m) <= 12:
                    if d.isdigit() == True and int(d) >= 1 and int(d) <= 31:
                        if y.isdigit() == True and int(y) >= 1 and len(y) == 4:
                            return (f'{int(y):04}-{int(m):02}-{int(d):02}')
            except(ValueError, KeyError):
                pass
        else:
            pass



main()