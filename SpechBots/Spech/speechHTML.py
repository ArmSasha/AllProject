#!/usr/bin/env python
# -*- coding: utf-8 -*-
import speech_recognition

sr = speech_recognition.Recognizer()
sr.pause_threshold = 1


commands_dict = {
	'commands': {
		'greeting': ['привет', 'приветствую'],
		'create_task': ['добавить задачу', 'создать задачу', 'заметка']
	}
}


def listen_command():
	"""The function will return the recognized command"""

	try:
		print("Speek: ")

		with speech_recognition.Microphone() as mic:
			sr.adjust_for_ambient_noise(mic, duration=1)
			audio = sr.listen(mic)
			query = sr.recognize_google(audio, language="ru-RU").lower()
			print(f"Вы сказали: {query}")
		return query

	except speech_recognition.UnknownValueError:
		return 'Damn... Технические шоколадки'


def greeting():
	"""Greeting function"""
	return 'Hi'


def create_task():
	"""Create a todo task"""

	print('Что добавим в список дел?')

	query = listen_command()

	with open('todo-list.txt', 'a') as file:
		file.write(f'{query}\n')

	return f"Задача '{query}' добавлена в todo-list!"


def main():
	query = listen_command()

	for k, v in commands_dict['commands'].items():
		if query in v:
			print(globals()[k]())


if __name__ == '__main__':
	main()


