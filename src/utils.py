import csv
from faker import Faker
from email_validator import validate_email, EmailNotValidError

# Create a Faker object that generates random data
fake = Faker()


def generate_fake_users_csv(csv_file: str) -> None:
    """Generate a CSV file with fake user data"""
    
    num_records = 1010
    columns = ["user_id", "name", "email", "signup_date"]
    
    with open(csv_file, mode='w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        
        for user_id in range(num_records):
            if user_id % 4 == 0:
                email = fake.email(domain="yahoo.com")
            elif user_id % 3 == 0:
                email = fake.email(domain="gmail.com")
            elif user_id % 7 == 0:
                email = fake.email(domain="hotmail.com")
            else:
                email = fake.email()  # I will consider this (example domain) as invalid email
            name = fake.name()
            signup_date = fake.date_time_this_decade().strftime("%Y-%m-%d %H:%M:%S")
            writer.writerow([user_id, name, email, signup_date])


def _format_date(date: str) -> str:
    """Format the date from timestamp to YYYY-MM-DD"""
    
    return date.split(" ")[0]


def is_valid_email(email: str) -> bool:
    """Check if an email is valid"""
    
    try:
        validate_email(email)
        return True
    except EmailNotValidError:
        return False


def get_email_domain(email: str) -> str:
    """Extract the domain from an email address"""
    
    return email.split("@")[1]
