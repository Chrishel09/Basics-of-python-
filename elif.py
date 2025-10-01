def main():
     color = "red"
     user = input("Enter a color: ")
     match user:
         case "red":
             print("color is red")
         case "blue":
             print("color is blue")
         case _:
             print("color not found")
main()