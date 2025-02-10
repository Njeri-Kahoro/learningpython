class dad:
    def football(self):
        print('Dad likes watching football')

class mum:
    def cooking(self):
        print('Mum likes cooking')

class boy(dad):
    def boy_age(self):
        print('The Boy is 15 years old')

class girl (mum):
    def girl_age(self):
        print('The Girl is 10 years old')



my_boy = boy()
my_boy.football()
my_boy.boy_age()

my_girl = girl()
my_girl.cooking()
my_girl.girl_age()