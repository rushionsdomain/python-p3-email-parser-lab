import re

class EmailAddressParser:
    '''Class to parse email addresses from a string.'''

    def __init__(self, input_string):
        '''Instantiates with a single argument, a string.'''
        self.input_string = input_string

    def parse(self):
        '''Parses the input string for valid email addresses.'''
        # Regular expression to match valid email addresses
        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
        
        # Find all matches of the email pattern in the input string
        matches = re.findall(email_pattern, self.input_string)

        # Use a list to preserve the order and remove duplicates
        unique_emails = []
        seen = set()

        for email in matches:
            if email not in seen:
                seen.add(email)
                unique_emails.append(email)

        return unique_emails
