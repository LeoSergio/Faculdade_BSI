def is_valid_date(date_str):
    try:
        day, month, year = date_str.split("/")  # Split by '/' separator
        day, month, year = int(day), int(month), int(year)  # Convert to integers

        # Check for valid day values
        if not 1 <= day <= 31:
            return False

        # Check for valid month values and adjust day range accordingly
        if not 1 <= month <= 12:
            return False
        elif month == 2 and not is_leap_year(year):  # Handle February for non-leap years
            if day > 28:
                return False
        elif month in [4, 6, 9, 11] and day > 30:
            return False

        # Check for valid year values
        if year < 1:
            return False

        return True  # All checks passed, date is valid

    except ValueError:  # Handle invalid input format
        return False

    except Exception as e:  # Handle unexpected errors
        print(f"Error during date validation: {e}")
        return False

def is_leap_year(year):

    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    return True
data_nasc = str(input(" Data de Nascimento: "))
while not is_valid_date(data_nasc):
        print("Data Inválida! Tente Novamente.\n(Insira a Data no Formato: xx/xx/xxxx)")
        print()
        data_nasc = str(input("-> "))
        data_nasc = data_nasc.strip()
print()