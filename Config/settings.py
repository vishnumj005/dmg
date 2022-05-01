import time


class NameGenerator:
    def get_name(self):
        return str(time.time())


name = NameGenerator()


class Environment:
    url = "https://automationpractice.com/"
    signup_email = "vishnu" + name.get_name() + "@mj.com"
    email = "vijayvichu.007@gmail.com"
    password = "vishnumj"
    f_name = "Vishnu"
    l_name = "M J"
    company = "SurveySparrow"
    address_1 = "Infopark Phase 2"
    city = "Kochi"
    state = "Kentucky"
    postcode = "00000"
    country = "India"
    mobile = "8714457241"
