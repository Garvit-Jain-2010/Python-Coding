# sentence = input("Enter a sentence: ")
# words = sentence.split()
# reversed_sentence = ' '.join(reversed(words))
# print("Reversed sentence:", reversed_sentence)

class Employee:
    a = 1
    
    @classmethod
    def show(cls):
        print(f"The class attribute of a is {cls.a}")

e = Employee()
e.a = 45

e.show()