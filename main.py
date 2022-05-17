import re
import random


def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response


def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float(len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False

    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0


def check_all_messages(message):
    highest_prob = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]):
        nonlocal highest_prob
        highest_prob[bot_response] = message_probability(
            message, list_of_words, single_response, required_words)

    response('¡Hola!, Bienvenido a mi bot. ¿Qué más pues?', [
             'hola', 'buenas', 'oe', 'holi', 'ola'], single_response=True)
    response('Bien y ¿vos como vas?', [
             'como', 'estas', 'va', 'vas', 'sientes', 'que', 'mas', 'pues'], single_response=True)
    response('Bien, muchas gracias por preguntar', [
             'bien', 'y', 'vos', 'tu'], single_response=True)
    response('Me alegra mucho', ['bien',
             'a', 'dios'], single_response=True)
    response('Si, la tecnología avanza con a pasos agigantados', [
             'bot'], single_response=True)
    response('Con mucho gusto', [
             'Muchas', 'Gracias', 'Agradecido', 'Chao', 'Todo bien'], single_response=True)

    best_match = max(highest_prob, key=highest_prob.get)
    print(highest_prob)

    return unknown() if highest_prob[best_match] < 1 else best_match


def unknown():
    response = ['¿Podrías repetir lo que me quieres decir?',
                'No entiendo lo que me quieres decir'][random.randrange(2)]
    return response


while True:
    print("Bot: " + get_response(input('You: ')))
