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


test = Cheker()
test.run()
