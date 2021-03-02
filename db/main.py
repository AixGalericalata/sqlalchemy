user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
user.hashed_password = "cap"
sesssion = db_session.create_session()
session.add(user)
session.commit()

user1 = User()
user1.surname = "Andrey"
user1.name = "Ridley"
user1.age = 20
user1.position = "captain"
user1.speciality = "research engineer"
user1.address = "module_1"
user1.email = "andrey_chief@mars.org"
user1.hashed_password = "cap"
session.add(user1)
session.commit()

user2 = User()
user2.surname = "Evgeniy"
user2.name = "Ridley"
user2.age = 19
user2.position = "captain"
user2.speciality = "research engineer"
user2.address = "module_1"
user2.email = "evgeniy_chief@mars.org"
user2.hashed_password = "cap"
session.add(user2)
session.commit()

user3 = User()
user3.surname = "Lexa"
user3.name = "Ridley"
user3.age = 18
user3.position = "captain"
user3.speciality = "research engineer"
user3.address = "module_1"
user3.email = "lexa_chief@mars.org"
user3.hashed_password = "cap"
session.add(user3)
session.commit()
