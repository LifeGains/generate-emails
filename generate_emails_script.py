def generate_emails(names):
    emails = []
    for name in names:
        # Split the name string into its components
        parts = name.split()
        firstname, lastname, company = parts[0], parts[1], parts[2]

        # Remove any spaces and convert to lowercase for standard email format
        firstname_clean = firstname.replace(" ", "").lower()
        lastname_clean = lastname.replace(" ", "").lower()
        company_clean = company.replace(" ", "").lower()

        # Generate the email addresses
        emails.append(f"{firstname_clean[0]}{lastname_clean}@{company_clean}.com")
        emails.append(f"{firstname_clean}{lastname_clean[0]}@{company_clean}.com")
        emails.append(f"{firstname_clean}{lastname_clean}@{company_clean}.com")
        emails.append(f"{firstname_clean}@{company_clean}.com")

    return emails

names_list = \
    ["firstname lastname company", 
     "firstname lastname company", 
     "firstname lastname company"]
all_emails = generate_emails(names_list)
for email in all_emails:
    print(email)