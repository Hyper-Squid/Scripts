number = int(input("Zadaj aky velky chces mat trojuholnik od 1 do 10: "))

if number > 10:
    print("To nemozes spravit!")
else:
    for i in range(1, number + 1):
        print("*" * i)