class ReverseString:
    def __init__(self, str):
        self.reversed = ""
        for i in range(len(str) - 1, -1, -1):
            self.reversed += str[i]

    def display(self):
        print("Reversed string: " + self.reversed)

if __name__ == "__main__":
    obj = ReverseString("Hello World")
    obj.display()
