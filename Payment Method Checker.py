accepted_payment = ("cash","gcash","card")

payment = input("What is your payment method?: ").lower()

if payment in accepted_payment:
    print("Valid payment method")

else:
    print("Invalid payment method")