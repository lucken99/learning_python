import sys
import requests
from bs4 import BeautifulSoup
how_many_examples = 5

arguments = sys.argv
if len(arguments) == 4:
	first_lang = arguments[1].lower()
	second_lang = arguments[2].lower()
	user_word = arguments[3].lower()
else:
	print("usage: script.py english german(or all for all) word")



languages = {'1': 'Arabic', '2': 'German', '3': 'English', '4': 'Spanish',
				'5': 'French', '6': 'Hebrew', '7': 'Japanese', '8': 'Dutch',
				'9': 'Polish', '10': 'Portuguese', '11': 'Romanian', '12': 'Russian',
				'13': 'Turkish'
				}
if second_lang == 'all':
	how_many_examples = 1
	second_lang = list(languages.values())
	language = [first_lang+'-'+i.lower() for i in second_lang if i.lower() != first_lang.lower()]
else:
	language = [first_lang+'-'+second_lang]


# # url = 'https://context.reverso.net/translation/english-french/'
# # print('Type "en" if you want to translate from French into English, \
# # 		or "fr" if you want to translate from English into French')

# print("Hello, you're welcome to the translator. Translator supports:")
# for key, val in languages.items():
# 	print(f'{key}. {val}')
# print("Type the number of your language:")
# try:
# 	first_lang = languages.get(input().strip()).lower()
# except:
# 	print("Enter valid number!")

# print("Type the number of language you want to translate to or '0' tp translate to all languages: ")
# is_zero = int(input())
# if is_zero == 0:
# 	how_many_examples = 1
# 	second_lang = list(languages.values())
# else:
# 	try:
# 		second_lang = languages.get(str(is_zero)).lower()
# 	except:
# 		print("Enter valid number!")
# if is_zero:
# 	language = [first_lang+'-'+second_lang]
# else:
# 	language = [first_lang+'-'+i.lower() for i in second_lang if i.lower() != first_lang.lower()]
# # print(language)


# print("Type the word you want to translate: ")
# user_word = input()



for lang in language:
	url = f'https://context.reverso.net/translation/{lang}/{user_word}'
	# print(url)

	if (lang.split('-')[0].title() not in languages.values()) or (lang.split('-')[1].title() not in languages.values()):
		print(f"Sorry, the program doesn't support {lang.split('-')[1]}")
		break

	r = requests.get(url, headers={'user-agent': 'lucky'})

	
	
	# print(r.status_code)
	try:
		if 200 <= r.status_code < 400:
			# print("200 OK\n")
			src = r.content
			soup = BeautifulSoup(src, 'html.parser')
			# words = soup.find_all('div', {'class': 'wide-container', 'id': 'translations-content'})
			translations = soup.find('div', {'class': 'wide-container', 'id': 'translations-content'}).text.split()
			examples = [i.strip() for i in soup.find('section', {'class': 'wide-container', 'id': 'examples-content'}).text.split('\n') if i ]
			
			# print("Context examples:\n")
			fl = open(f'{user_word}.txt', 'a+', encoding='utf-8')
			print(f"{lang.split('-')[1].title()} Translations:", file=fl)
			print(f"{lang.split('-')[1].title()} Translations:")
			try:
				for i in range(how_many_examples):
					print(translations[i], file=fl)
					print(translations[i])
			except:
				pass

			print(f"\n{lang.split('-')[1].title()} Examples:", file=fl)
			print(f"\n{lang.split('-')[1].title()} Examples:")
			try:
				for i in range(0, how_many_examples*2, 2):
					print(examples[i]+':', file=fl)
					print(examples[i+1], file=fl)
					print(file=fl)
					print(examples[i]+':')
					print(examples[i+1])
					print()
			except:
				pass
			fl.close()
			r.close()

		else:
			# print(r.status_code)
			print(f"Sorry, unable to find {user_word}")
			break
	except Exception:
		print(r.status_code)
		print("Something wrong with your internet connection")