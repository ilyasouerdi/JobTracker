import datetime

class User :

   def __init__(self,
                id: int,
                name : str,
                email : str,
                pass_word_hash : str,
                created_at: datetime.datetime
                ):
        self.id = id
        self.name = name
        self.email = email
        self.pass_word_hash = pass_word_hash
        self.created_at = created_at


   @staticmethod
   def from_dict(data):
       user = User(
           id = data["id"],
           name = data["name"],
           email = data["email"],
           pass_word_hash = data["password_hash"],
           created_at=datetime.datetime.fromisoformat(
                data["created_at"])
       )
       return user

   
   def to_dict(self):
       return { 
           "id": self.id,
           "name": self.name,
           "email": self.email,
           "password_hash": self.pass_word_hash,
           "created_at": self.created_at.isoformat() 
           }






class Company:

    def __init__(self,
                 id : int,
                 name : str,
                 website : str,
                 location : str,
                 industry : str):
        self.id = id
        self.name = name
        self.website = website
        self.location = location 
        self.industry = industry
   
    def to_dict(self):
       return {
           "id": self.id,
           "name": self.name,
           "website": self.website,
           "location": self.location,
           "industry": self.industry 
        } 
    @staticmethod
    def from_dict(data):
        company = Company(
            id=data["id"],
            name=data["name"],
            website=data["website"],
            location=data["location"],
            industry=data["industry"]
        )
        return company
           


      
class Application:
    def __init__(self,
                 id : int,
                 user_id : int,
                 company_id : int,
                 position : str,
                 status : str,
                 date_applied : datetime.datetime ,
                 salary_expected : float,
                 note : str
                 ):
        self.id = id 
        self.user_id = user_id
        self.company_id = company_id
        self.position = position 
        self.status = status
        self.date_applied = date_applied
        self.salary_expected = salary_expected
        self.note = note
        
    def to_dict(self):
       return {
           "id": self.id,
           "user_id": self.user_id,
           "company_id": self.company_id,
           "position": self.position,
           "status": self.status,
           "date_applied": self.date_applied.isoformat(),
           "salary_expected": self.salary_expected,
           "note": self.note 
        }
    @staticmethod
    def from_dict(data):
        application =Application(
            id=data["id"],
            user_id=data["user_id"],
            company_id=data["company_id"],
            position=data["position"],
            status=data["status"],
            date_applied=datetime.datetime.fromisoformat(
                data["date_applied"]
            ),
            salary_expected=data["salary_expected"],
            note=data["note"]
        )
        return application 
status = ["Applied", "Interview", "Rejected", "Accepted"]