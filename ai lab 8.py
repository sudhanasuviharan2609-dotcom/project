database = ["Croaks", "Eat Flies", "Shrimps", "Sings"]
knowbase = ["Frog", "Canary", "Green", "Yellow"]

def display():
    print("\nX is:")
    print("1. Croaks")
    print("3. Shrimps")
    print("4. Sings")
    print("Select One: ", end='')

def main():
    print("-----Forward Chaining-----")
    display()
    try:
        x = int(input())
        print()
        
        if x == 1 or x == 2:
            print("Chance of Frog")
            print(f"X is {database[x-1]}")
            print("\nColor is:")
            print("1. Green")
            print("2. Yellow")
            print("Select Option: ", end='')
            k = int(input())
            
            if k == 1:
                print(f"Yes it is {knowbase[0]} and Color is {knowbase[2]}")
            elif k == 2:
                print("Invalid Knowledge Base")
            else:
                print("Invalid Color Option")
                
        elif x == 3 or x == 4:
            print("Chance of Canary")
            print(f"X is {database[x-1]}")
            print("\nColor is:")
            print("1. Green")
            print("2. Yellow") 
            print("Select Option: ", end='')
            k = int(input())
            
            if k == 2:
                print(f"Yes it is {knowbase[1]} and Color is {knowbase[3]}")
            elif k == 1:
                print("Invalid Knowledge Base")
            else:
                print("Invalid Color Option")
                
        else:
            print("Invalid Option Selected")
            
    except ValueError:
        print("Please enter a valid number")

if __name__ == "__main__":
    main()