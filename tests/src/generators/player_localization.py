from faker import Faker

fake=Faker()



class PlayerLocalization:
    def __init__(self,lang):
        self.faker = Faker(lang)
        self.result = {
            "nickname": self.faker.first_name(),
            }

    def set_number(self,number=11):
        self.result['number'] = number
        return self

    def polish_language(self,lang="pl_PL"):
        self.faker = Faker(lang)
        self.result['PL_nickname'] = self.faker.first_name()
        return self

    def build(self):
        return self.result
    

    print(Faker("fr_FR").first_name())
