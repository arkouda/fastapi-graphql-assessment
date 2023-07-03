import strawberry
from models import User
import datetime

@strawberry.type
class UserType:
    id: int
    name: str
    email: str
    date_registered: datetime.date

@strawberry.input
class UserInput:
    name: str
    email: str

@strawberry.type
class Query:
    @strawberry.field
    def get_user_by_id(self, info, id: int) -> UserType:
        # Add code to get a user by their ID
        pass

    @strawberry.field
    def get_all_users(self, info) -> list[UserType]:
        # Add code to get all users
        pass

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, info, user_data: UserInput) -> UserType:
        # Add code to create a user
        pass

schema = strawberry.Schema(query=Query, mutation=Mutation)
