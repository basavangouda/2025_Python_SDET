import random
import string


def generate_random_email(domain="example.com", length=10):
   characters = string.ascii_lowercase + string.digits
   username = ''.join(random.choice(characters) for i in range(length))
   print(username+'@'+domain)
   return f"{username}@{domain}"





