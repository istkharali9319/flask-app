def mask_email(email):
    if "@" not in email:
        return email

    name, domain = email.split("@", 1)
    if len(name) <= 2:
        return f"{name[0]}***@{domain}"

    return f"{name[:2]}***@{domain}"
