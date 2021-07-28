import random
import time
import speech_recognition as sr

def recognize_speech_mic(recognizer, microphone):

    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` must be `Microphone` instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    # response object
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # if a RequestEror or UnknownValueError exception is caught, update response
    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        response["success"] = False
        response["error"] = "API unaviable"
    except sr.UnknownValueError:
        response["error"] = "Unable to recognize speech"

    return response

if __name__ == "__main__":
    NAMES = ["thomas", "pablo", "benjamin", "jane", "robert"]
    NUM_GUESSES = 3

    # create recognizer and mic instances
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # random word from the list
    name = random.choice(NAMES)

    # format the instructions string
    instructions = (
        "I'm thinking of one of the these names:\n"
        "{names}\n"
        "You have {n} tries to guess which one.\n"
    ).format(names=', '.join(NAMES), n=NUM_GUESSES)


    # show instructions and wait 3 seconds before starting the game
    print(instructions)
    time.sleep(3)

    for i in range(NUM_GUESSES):
        for j in range(len(NAMES)):
            print('Guess {}. Speak!'.format(i+1))
            guess = recognize_speech_mic(recognizer, microphone)
            if guess["transcription"]:
                break
            if not guess["success"]:
                break
            print("I didn't catch that. What did you say?\n")

            if guess["error"]:
                print("ERROR: {}".format(guess["error"]))






