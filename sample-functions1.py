import requests

class FromFunction1:
    def fetch_all_books(self):
        response = requests.get(url="http://127.0.0.1:5000/v1/resources/books/all")
        return response
        

if __name__ == '__main__':
    response = FromFunction1().fetch_all_books()
    print(response.json())

'''
 
class FromFunction:
 
    # # constructor of Main class
    # def __init__(self):
    #     # Initialization of the Strings
    #     self.String1 ="Hello"
    #     self.String2 ="World"
 
    def fetch_all_books(self):
        response = requests.get(url="http://127.0.0.1:5000/v1/resources/books/all")
        return response
 
    def Function2(self):
        print("Function2 : hello")
        return

if __name__ == '__main__': 
    # Instance of Class Main
    Object = FromFunction()
    
    # Calling Function1
    response = Object.fetch_all_books()
    print(response.json())
    '''