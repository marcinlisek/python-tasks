def candies_calculator():

    no_of_entries = int(input("Enter how many data sets you want to provide: "))
    
    print("")
    
    results = []
    
    numbers = [0, 0]

    for entry in range(1, no_of_entries+1):
        while numbers[0] not in range(10, 31) or numbers[1] not in range(10, 31):
            numbers = input("Enter the number of kids in the first group: ").split()
            num1 = int(numbers[0])
            num2 = int(numbers[1])

            for multiplier in range(1, 101):
                if (multiplier * num1) % num2 == 0 and (multiplier * num1) % 2 == 0:
                    results.append(multiplier * num1)
                    break

    return results


candies_number = candies_calculator()
counter = 0
print("")
for x in candies_number:
    counter += 1
    print(f"In the {counter} group the teacher needs {x} candies.")
