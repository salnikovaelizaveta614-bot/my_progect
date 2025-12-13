from string import digits
from datetime import*
from re import*


def required(value):
    return value is not None


def parse_text(value: str):
    return value if len(value.strip()) > 0 else None


def parse_int(value: str):
    value = value.strip()
    if len(value) == 0:
        return None

    if value[0] == "-":
        is_negative = True
        value = value[1:]
    else:
        is_negative = False

    for s in value:
        if s not in digits:
            return None

    return -int(value) if is_negative else int(value)


def parse_date(value):
    if len(value)==0:
        return None
    data = fullmatch(r'(\d{1,2})\.(\d{1,2})\.(\d{4})',value)
    if data:
        day, month, year = data.groups()
        data = [int(day), int(month), int(year)]
        return data
    else:
        return None
    

def phone(value):
    if len(value)==0:
        return None
    phone_number = fullmatch(r'\+7\d{10}',value)
    if phone_number:
        return phone_number.group()
    return None


def email(value):
    email_adress= fullmatch(r'\w+@\w+\.[a-zA-Z]{2,}',value)
    if email_adress:
        return True
    return False


def min_value(min_length):
    def validator(value):
        return value >= min_length
    return validator


def max_value(max_length):
    def validator(value):
        return value <= max_length
    return validator


def min_length(min_length):
    def validator(value):
        return len(value) >= min_length
    return validator


def max_length(max_length):
    def validator(value):
        return len(value) <= max_length
    return validator


def date_limit(max_data, min_data):
    def validator(data):
        day, month, year = data
        if 1<=day<=31 and 1<=month<=12 and year>1000:
            data = date(year, month, day)
            return min_data<=data<=max_data
        else:
            return False
    return validator


def compose(*validators):
    def validator(value):
        for validator in validators:
            if not validator(value):
                return False
        return True
    return validator

def single_validator(parse, validate):
    def validator(value): 
        return validate(parse(value))
    return validator

phone_validator = single_validator(
  parse_text, compose(required, phone)
)
score_validator = single_validator(
  parse_int, compose(required, max_value(100))
)
birthdate_validator = single_validator(
  parse_date, compose(required,date_limit(date.today(),date(1900,12,31)))
)
email_validator = single_validator(parse_text, compose(required,email))

print(phone_validator("+79005553535"))
print(phone_validator("abrada"))
print(score_validator("60"))
print(birthdate_validator("30.06.2007"))
print(email_validator("a@a.aa"))



# min_value_validator = min_value(10)
# max_value_validator = max_value(999)

# parsed_int = parse_int(input())
# is_valid_int = required(parsed_int) and min_value_validator(parsed_int) and max_value_validator(parsed_int)

# max_length_validator = max_length(30)
# min_length_validator = min_length(10)


# parsed_text = parse_text(input())
# is_valid_text = required(parsed_text) and min_length_validator(parsed_text) and max_length_validator(parsed_text)
