from client import authenticate

if __name__ == "__main__":
    access_token = authenticate()
    print("Access token:", access_token)
