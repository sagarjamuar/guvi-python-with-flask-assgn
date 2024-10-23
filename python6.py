import re

def validate_emails(email_list):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return [email for email in email_list if re.match(pattern, email)]

signups = [
    'john.doe@example.com', 'invalid-email', 'jane_doe123@website.org',
    'user@domain', 'alice@company.com', 'bob@invalid-email.'
]

valid_emails = validate_emails(signups)
print(valid_emails)
