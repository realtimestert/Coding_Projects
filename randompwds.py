import secrets
import time

def main() -> int | None:

    num_str = input("Enter the number of required characters in the new password: ")
    try:
        length = int(num_str)
        return length
    except ValueError:
        print("Not a valid number. ")
        return None

if __name__ == "__main__":
    pwd_length = main()

    if pwd_length is not None:
        print(f"The value you entered is {pwd_length}")
        generated_pw = secrets.token_urlsafe(pwd_length)
        print("Genereated password: ", generated_pw)
    
        with open("passwords.txt", "a", encoding="utf-8") as f:
            f.write(f"{pwd_length}\t{generated_pw}\n")
        print("Password saved to passwords.txt")
        print("Ending program in 10 seconds... copy that password to use")
        time.sleep(10)