class Hello:
    def greet(self):
        print("Hello from the Hello class!")

    def tptint(self):
        print("This is the tptint method from Hello class")

class NewHello(Hello):
    def greet(self):
        super().greet()
        print("And hello from the NewHello class!")