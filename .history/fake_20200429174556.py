from faker import Faker
fake = Faker()
for _ in range(10):
    print('{\'title\':\''+fake.name()+'\',\'year\':“'+fake.year()+'\'},')