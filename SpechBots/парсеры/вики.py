import wikipedia

wikipedia.set_lang("ru")

if __name__ == '__main__':
	while True:
		text_to_search = input("Что искать? ")
		search_results = wikipedia.search(text_to_search, results=5)

		if len(search_results) == 0 or text_to_search == 'exit':
			print(f"По запросу '{text_to_search}' ничего не найдено")
			exit()

		for index, result in enumerate(search_results):
			print(f"{index}) {result}")

		get_one = input("Номер результата: ")
		search_result = search_results[int(get_one)]
		text = wikipedia.summary(search_result)

		print(text)