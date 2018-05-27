print("Reboot the computer and try to connect.")
computerReboot = input("Did that fix the problem? Yes or No.")

# I think a variable response will be less redundant that typing the same
# response multiple times.
problemResolved = "Yay!! Problem solved."

if computerReboot == "No":
    print("Reboot the Router and try to connect.")
    routerReboot = input("Did that fix the problem? Yes or No.")

    if routerReboot == "No":
        print("Make sure the cables between the router and modem \
are plugged in firmly.")
        computerCables = input("Did that fix the problem? Yes or No.")
        
        if computerCables == "No":
            print("Move the router to a new location.")
            moveRouter = input("Did that fix the problem? Yes or No.")

            if moveRouter == "No":
                print("Get a new router.")

            else:
                print(problemResolved)

        else:
            print(problemResolved)

    else:
        print(problemResolved)

else:
    print(problemResolved)

print("Doug Lamar")
