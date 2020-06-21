import requests
import hashlib
def hasher(password):
    hasher = hashlib.sha1(str(password).encode())
    hashed_pswrd = hasher.hexdigest().upper()
    return hashed_pswrd

def request_response(hashed_pswrd):
    url = "https://api.pwnedpasswords.com/range/" + hashed_pswrd[:5]
    res = requests.get(url)
    response = res.text
    tail = hashed_pswrd[5:]
    return checker(response,tail)

def checker(response,tail):
    k = (line.split(":") for line in response.splitlines())
    for h,count in k:
        if h == tail:
            return count
    return -1

def main(m):
    l = hasher(m)
    z = request_response(l)
    if z == -1:
        return "YOU HAVE A STRONG PASSWORD"
    else:
        return f"CHANGE THE PASSOWORD, IT HAS EXPOSED {z} TIMES"


x = input("Enter your password to check: ")
print(main(x))

