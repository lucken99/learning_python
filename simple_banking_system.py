import sys
from random import randint
import sqlite3



conn = sqlite3.connect("card.s3db")

cur = conn.cursor()

cur.execute("create table if not exists card (id integer not null , number text primary key, pin text not null, balance integer default 0);")

conn.commit()





#takes card number as string without checksum and returns checksum
def luhn_algo(string_card_num):
	number = list(map(int, string_card_num))
	length = len(number)

	for i in range(1, len(number)+1):
		if i&1:
			number[i-1] *= 2
	sums = 0
	for i in range(length):
		if number[i] > 9:
			number[i] -= 9
	sums = sum(number)

	if (sums % 10) == 0:
		return '0'
	else:
		return str(10 - (sums % 10))

def checkLuhn(cardNo):
     
    nDigits = len(cardNo)
    nSum = 0
    isSecond = False
     
    for i in range(nDigits - 1, -1, -1):
        d = ord(cardNo[i]) - ord('0')
     
        if (isSecond == True):
            d = d * 2
  
        # We add two digits to handle
        # cases that make two digits after
        # doubling
        nSum += d // 10
        nSum += d % 10
  
        isSecond = not isSecond
     
    if (nSum % 10 == 0):
        return True
    else:
        return False




class CreditCard:
	
	credit_cards = {}
	
	def __init__(self):
		
		self.issuer_id_num = str(400000)
		# self.account_id = str(randint(100000000, 999999999))
		self.account_id = ''.join(["{}".format(randint(0, 9)) for num in range(9)])
		# self.pin = str(randint(1000, 9999))
		self.pin = ''.join(["{}".format(randint(0,9)) for num in range(4)])
		# self.checksum = str(randint(0, 9))
		self.checksum = luhn_algo(self.issuer_id_num + self.account_id)
		self.card_num = self.issuer_id_num + self.account_id + self.checksum
		CreditCard.credit_cards[self.card_num] = self.pin
		
		cur.execute(f"insert into card (id, number, pin, balance) values({len(CreditCard.credit_cards)}, {self.card_num}, {self.pin}, 0)")
		conn.commit()

	def print_credentials(self):
		print("\nYour card has been created")
		print(f"Your card number:\n{self.card_num}")
		print("Your card PIN:")
		print(self.pin)
		# cur.execute("select * from card")
		# print(cur.fetchall())

	def validate_credentials(self, user_card_num, user_pin):
		# pin = CreditCard.credit_cards.get(user_card, None)
		# if pin and (pin == user_pin):
		# 	return True
		# return False

		cur.execute(f"select number, pin from card where (number = {user_card_num}) and pin = {user_pin}")
		if cur.fetchall():
			return True
		return False




while True:
	print("1. Create an account\n2. Log into account \n0. Exit")
	user_input1 = input().strip()

	if user_input1 == '0':
		print("\nBye!")
		sys.exit()

	if user_input1 == '1':
		card = CreditCard()
		card.print_credentials()
		print()
	elif user_input1 == '2':
		user_card_num = input("\nEnter your card number:\n").strip()
		user_pin = input("Your card PIN:\n").strip()
		card = CreditCard()
		status = card.validate_credentials(user_card_num, user_pin)
		if status:
			print("\nYou have successfully logged in!")
			while True:
				print("\n1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
				user_input2 = input().strip()
				if user_input2 == '0':
					print("\nBye!")
					sys.exit()
				elif user_input2 == '1':
					cur.execute(f"select balance from card where number = {user_card_num} and pin = {user_pin}")

					print("\nBalance:", cur.fetchone()[0])
				elif user_input2 == '2':
					print("\nEnter income:")
					user_income_input = int(input())
					cur.execute(f"update card set balance = balance+{user_income_input} where number={user_card_num} and pin = {user_pin}")
					conn.commit()
					print("Income was added!")


				# transfer
				elif user_input2 == '3':
					print("\nTransfer")
					print("Enter card number:")
					reciever_card_num = input()
					if reciever_card_num == user_card_num:
						print("You can't transfer money to the same account!")
						continue
					if checkLuhn(reciever_card_num):
							cur.execute(f"select * from card where number={reciever_card_num}")
							if cur.fetchall():

								cur.execute(f"select balance from card where number={user_card_num} and pin = {user_pin}")
								curr_balance = cur.fetchone()[0]
								print("Enter How much money you want to transfer:")
								transfer_money = int(input())
								if transfer_money <= curr_balance:
									cur.execute(f"update card set balance = balance - {transfer_money} where number={user_card_num} and pin={user_pin}")
									cur.execute(f"update card set balance = balance + {transfer_money} where number = {reciever_card_num}")
									conn.commit()
									print("Success!")
									continue
								else:
									print("Not enough money!")
									continue
							else:
								print("Such a card does not exist.")
								continue
						
						
					else:
						print("Probably you made a mistake in the card number. Please try again!")
						continue

				# close account
				elif user_input2 == '4':
					cur.execute(f"delete from card where number = {user_card_num} and pin = {user_pin}")
					conn.commit()
					print("\nThe account has been closed!\n")
					break


				elif user_input2 == '5':
					print("\nYou have successfully logged out!\n")
					break


		else:
			print("\nWrong card number or PIN!\n")


