def withdraw_money(bank_balance, amount_to_withdraw):
bank_balance - amount_to_withdraw
def deposit_money(bank_balance, amount_to_deposit):
bank_balance + amount_to_deposit
def calculate_interest(bank_balance, interest_rate):
bank_balance *= interest_rate
def main():
bank_balance = 100
# Withdraw 10 euros from the bank balance
bank_balance_after_withdrawal = withdraw_money(bank_balance, 10)
# Deposit 20 euros to the bank balance
bank_balance_after_deposit = deposit_money(bank_balance, 20)
# Calculate the interest of the bank balance using the provided rate and increase the bank balance by that amount
bank_balance_after_interest_payment = calculate_interest(bank_balance, 0.5)
print(f"Final bank balance is {bank_balance}. It should be 165")
main()