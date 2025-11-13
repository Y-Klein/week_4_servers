from fastapi import FastAPI
import uvicorn

app = FastAPI()
items = []

@app.get("/test")
def testing():
    return {"msg": "hi from test"}


@app.get("/test/{name}")
def save_user(name):
    with open("names.txt","a") as names:
        names.write(name)
        names.write("\n")
    return { "msg": "saved user"}


@app.post("/caesar")
def caesar_cipher(text:str,offset:int,mode:str):
    ab = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    result = ""
    for i in text.lower():
        if i  in ab:
            if mode == "encrypt":
                result +=  ab[(ab.index(i) + offset) % (len(ab))]
            elif mode == "decrypt":
                result += ab[(ab.index(i) - offset) % (len(ab))]
        else:
            result += i
    return f"{mode}ed_text: {result}"

@app.get("/fence/encrypt")
def fence_cipher_encrypt(text:str):
    a = ""
    b = ""
    string = "".join(text.split())
    for i in range(len(string)):
            if i % 2 == 0:
                a += string[i]
            else:
                b += string[i]
    result = a + b
    return f"encrypted_text: {result}"

@app.post("/fence/decrypt")
def fence_cipher_decrypt(text):
    point = len(text) // 2 + (len(text) % 2 > 0)
    a = text[:point]
    a_point = 0
    b = text[point:]
    b_point = 0
    result = ""
    for i in range(len(text)):
        if i % 2 == 0:
            result += a[a_point]
            a_point += 1
        else:
            result += b[b_point]
            b_point += 1

    return f"decrypted_text: {result}"




if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)


