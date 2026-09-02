import re


def check_email(email):
    email_regexp = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"

    # Create new pattern for email validation
    email_check_pattern = re.compile(email_regexp)
    return (email, 'valid' if email_check_pattern.fullmatch(email) else 'invalid')


# Valid
print(check_email('matvii@gmail.com'))
print(check_email('matv_ii@gmail.com'))
print(check_email('matvi.i@gmail.com'))
print(check_email('mat.vii@ps.gmail.com'))

# Invalid
print(check_email('matviigmail.com'))
print(check_email('matvii@gmailcom'))
print(check_email('@gmail.com'))
print(check_email('matvii@'))
