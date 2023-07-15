def calculate_easter_date(year):
    if year < 1900 or year > 2099:
        raise ValueError("This program can calculate Easter dates only between 1900 and 2099.")
    
    a = year % 19
    b = year % 4
    c = year % 7
    k = year // 100
    p = (13 + 8 * k) // 25
    q = k // 4
    M = (15 - p + k - q) % 30
    N = (4 + k - q) % 7
    d = (19 * a + M) % 30
    e = (2 * b + 4 * c + 6 * d + N) % 7
    
    if d == 29 and e == 6:
        day = 19
        month = 4
    elif d == 28 and e == 6 and (11 * M + 11) % 30 < 19:
        day = 18
        month = 4
    else:
        day = 22 + d + e
        month = 3 if day > 31 else 4
    
    return f"{year}-{month:02d}-{day:02d}"

# Test the function
year = int(input("Enter the year (between 1900 and 2099): "))
easter_date = calculate_easter_date(year)
print("The date of Easter in {year} is {easter_date}.")
