def lucky_ticket(ticket_number):
    sum1 = 0
    sum2 = 0
    ticket_number1 = ticket_number//1000
    ticket_number2 = ticket_number%1000
    while ticket_number1!= 0:
        sum1+= ticket_number1%10
        ticket_number1 = ticket_number1//10
    while ticket_number2!= 0:
        sum2+= ticket_number2%10
        ticket_number2 = ticket_number2//10
    if sum2==sum1:
        return True
    else:
        return False

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))