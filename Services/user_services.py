from Models.user_model import User

class UserService:
    def create_user(self, firstname, lastname, age, cin, email, password):
        user = User(
            firstname=firstname,
            lastname=lastname,
            age=age,
            cin=cin,
            email=email,
            password=password
        )
        user.save()  
        return str(user.id)

    def get_user(self, user_id):
        user = User.objects(id=user_id).first()
        return user

    def update_user(self, user_id, **update_data):
        user = User.objects(id=user_id).first()  
        if user:
            for key, value in update_data.items():
                setattr(user, key, value)  
            user.save()  
            return True
        return False

    def delete_user(self, user_id):
        user = User.objects(id=user_id).first() 
        if user:
            user.delete() 
            return True
        return False
