# your code goes here!
def countdown(num: int) -> str:
    while(abs(num) > 0):
        print(f"{num} SECOND(S)!")
        num -= 1
    print("HAPPY NEW YEAR!")

import time
def countdown_with_sleep(num: int) -> str:
    while(abs(num) > 0):
        print(f"{num} SECOND(S)!")
        num -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")
    
if __name__ == "__main__":
    countdown_with_sleep(10, 1)