email=input("emter your email:")
username=email[email.index("@"):]
domain=email[:email.index("@")]
print(f"username is {username} and domain is {domain}")