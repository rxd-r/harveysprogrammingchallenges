def email_validator(email: str):
    errors = [] #my name is neung

    first_part: str = ""
    last_part: str = ""
    found_at: bool = False
    found_dot: bool = False

    for ch in email:
        if ch != '@':
            if not found_at:
                first_part += ch
            else:
                last_part += ch
        else:
            found_at = True

        if found_at and ch == '.':
            found_dot = True

    if first_part == "":
        errors.append("Empty user")

    if not found_at:
        errors.append("Missing @ symbol")
    elif last_part == "":
        errors.append("Empty domain")
    elif not found_dot:
        errors.append("Invalid domain")


    if len(errors) == 0:
        print("Valid Email :)")
    else:
        print("Invalid Email: ")
        for error in errors:
            print(f" - {error}")
