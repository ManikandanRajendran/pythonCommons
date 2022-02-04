import requests

class FromFunction2:
    def fetch_books_by(self, params, value):
        response = requests.get(url=f"http://127.0.0.1:5000/v1/resources/books?{params}={value}")
        return response


if __name__ == '__main__':
    response = FromFunction2().fetch_books_by("id", "0")
    print(response.json())