print("Hello user, my name is Fedya")
print("Soon I will make data entry in this program through the Docke container, but for now you can change the data in the code of my program (main.py)")



class Cheker():



    def run(self):
        a = 1
        b = 10

        print("Let's go ")
        while True:
            if a <= b:
                print(a)
                a = a + 1
            else:
                break

    def unrun(self):
        a = 1
        b = 10
        print("Now to the side")
        while True:
            if b >= a:
                print(b)
                b = b - 1
            else:
                break


test = Cheker()
test.run()
test.unrun()
