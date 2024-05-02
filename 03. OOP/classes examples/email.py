import re

class Email(object):
    def __init__(self, email_address):
        """
        Initializes an Email object with the provided email address.
        """
        self._email_address = email_address

    @property
    def email_address(self):
        """
        Getter method to retrieve the email address.
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self, new_email_adress):
        """
        Setter method to set a new email address after validating and converting it to lowercase.
        """
        if self.is_valid_email(new_email_adress):
            self._email_address = new_email_adress.lower()
        else:
            return ValueError("Invalid email address format.")
     
    def is_valid_email(self, email=None)-> bool:
        """
        Checks whether the provided email address is valid according to the defined regex pattern.
        """
        email = email if email else self._email_address
        pattern = r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        if re.match(pattern, email):
            return True
        else:
            return False
    
    def get_domain_name(self):
        """
        Retrieves the domain name from a valid email address.
        """
        if self.is_valid_email():
            return self._email_address.split('@')[1]
        else:
            return f"{self._email_address} is invalid"
    
    def get_user_name(self):
        """
        Retrieves the username from a valid email address.
        """
        if self.is_valid_email():
            return self._email_address.split('@')[0]
        else:
            return ValueError


email1 = Email("neo@gmail.com")
email1.email_address = 'NEON@gmail.com'
email2 = Email("check_email.com")

print(email1.get_user_name())
print(email1.is_valid_email(),'--->', email1.get_domain_name())
print(email2.is_valid_email(),'--->', email2.get_domain_name())
