class Auto:
    brand = ''
    age = 0
    color = ''
    mark = ''

    def move(self):
        print('move')

    def birthday(self):
        self.age += 1


    def stop(self):
        print('stop')

a,b,c = Auto(),Auto(),Auto()

a.birthday()
b.move()
c.stop()
print(a.age)

