with open ("hr_system.txt") as employee_line:
    for items in employee_line:
        parts = items.split()
        names = parts [0]
        id = parts [1]
        occupation = parts [2]
        salary = float (parts [3])
        pay_check = salary/24

        if occupation == "Engineer":
            pay_check += 1000
        print (f"{names},(ID: {id}), {occupation} - ${pay_check:.2f}")