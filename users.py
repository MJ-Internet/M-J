from werkzeug.security import generate_password_hash

USERS = {
    "admin1@company.com": generate_password_hash("StrongPassword1"),
    "admin2@company.com": generate_password_hash("StrongPassword2")
}
