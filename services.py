from datetime import datetime
from Models import User, Company, Application, status
import hashlib
import json

users = []
companies = []
applications = []

def password_hashing(password : str):
    return hashlib.sha256(password.encode()).hexdigest()


def create_user(name: str, email: str, password: str):
    try:
        user_id = len(users)+1
        hashed_password = password_hashing(password)
        user = User(
            id = user_id,
            name = name,
            email = email,
            pass_word_hash = hashed_password,
            created_at= datetime.now()
        )
        users.append(user)
    except Exception as e:
        print(f"error: {e}")
        return None
    return user


def login_user(email: str, password: str):
    hashed_password = password_hashing(password)
    try:
        for user in users:
            if user.email == email:
                if user.pass_word_hash == hashed_password:
                    return user
                return None
        return None

    except Exception as e:
        print(f"error: {e}")
        return None



def get_user_by_id(user_id: int):
        for user in users:
            if user.id == user_id:
                return user
        return None


def list_users():
        return users



def update_user(user_id: int, name: str, email: str, password: str):
        for user in users:
            if user.id == user_id:
                user.name = name
                user.email = email
                user.pass_word_hash = password_hashing(password)
                return user 
        return None

            

   

def delete_user(user_id: int):
    try:
        for user in users:
            if user.id == user_id:
                users.remove(user)
                return True
        return False

    except Exception as e:
        print(f"error: {e}")
        return False

#company services 

def create_company(
    name: str,
    website: str,
    location: str,
    industry: str
):
    company_id = len(companies)+1
    company = Company(
        id = company_id,
        name = name ,
        website = website,
        location = location, 
        industry = industry
    )

    companies.append(company)
    return company


def get_company_by_id(company_id: int):
    for company in companies :
        if company.id == company_id:
            return company

    return None
        
    


def list_companies():
    return companies


def search_companies(keyword: str):
    results = []
    keyword = keyword.lower()

    for company in companies:
        if (
            keyword in company.name.lower()
            or keyword in company.location.lower()
            or keyword in company.industry.lower()
        ):
            results.append(company)
        
    return results


def update_company(company_id: int, name: str, website: str, location: str, industry: str):
    for company in companies:
        if company.id == company_id:
            company.name = name
            company.website = website
            company.location = location
            company.industry = industry
            return company
    return None




def delete_company(company_id: int):
    for company in companies:
        if company.id == company_id:
            companies.remove(company)
            return True
    return False

#Application services 

def apply_to_company(
    user_id: int,
    company_id: int,
    position: str,
    salary_expected: float,
    note:str
):
    try:
        user = get_user_by_id(user_id)
        company = get_company_by_id(company_id)
        if user == None or company == None:
            return None 
        application_id = len(applications)+1
        application = Application(
            id = application_id,
            user_id = user.id,
            company_id = company.id,
            position = position,
            salary_expected = salary_expected,
            status = "Applied",
            date_applied=datetime.now(),
            note = note
        )
        applications.append(application)
        return application
    except Exception as e :
        print(f"error: {e}")

    


def get_application_by_id(application_id: int):
    for application in applications:
        if application.id == application_id:
            return application
    return None


def list_applications():
    return applications


def list_user_applications(user_id: int):
    results = []
    for application in applications:
        if application.user_id == user_id:
            results.append(application)
    return results
               


def update_application_status(
    application_id: int,
    new_status: str
):
    if new_status in status :
        for application in applications:
            if application.id == application_id:
                application.status = new_status
                return application
        return None


def delete_application(application_id: int):
    for application in applications:
        if application.id == application_id:
            applications.remove(application)
            return True
    return False


def filter_applications_by_status(status: str):
    results = []
    for application in applications:
        if application.status == status:
            results.append(application)
    return results


# Utility services 


def save_data():
    user_json = []
    companies_json = []
    applications_json = []

    for user in users:
        user_json.append(user.to_dict())
    for company in companies:
        companies_json.append(company.to_dict())
    for application in applications:
        applications_json.append(application.to_dict())
    
    with open("users.json", "w") as u:
        json.dump(user_json,u, indent=4)
    with open("companies.json","w") as c:    
        json.dump(companies_json,c,  indent=4)
    with open("applications.json", "w") as a:
        json.dump(applications_json,a, indent=4)

    return True


def load_data():
    pass


def export_to_csv():
    pass


def generate_statistics():
    pass