# The `Worker` interface forces all subclasses to implement `work()`, `eat()`, `sleep()`, and `get_salary()`.  
# Problem: Robots don’t eat or sleep, so `Robot` must implement meaningless methods. This **violates the Interface Segregation Principle (ISP)** because clients are forced to depend on methods they don’t use.

# ------------------------------------------------------------
class Human:
    def work(self):
        print("Human working")

    def eat(self):
        print("Human eating")

    def sleep(self):
        print("Human sleeping")

    def get_salary(self):
        print("Human gets salary")


class Robot:
    def work(self):
        print("Robot working")

    def get_salary(self):
        print("Robot gets salary")