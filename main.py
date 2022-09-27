# initial idea by Technolus#1800, started as a joke:
# "so I can link that to an animation on the avatar and say "MEGAZORD ACTIVATEEEEEEE!!!!"
# and my avatar will start some transformation sequence?"
# I was like "sure", so here it is
from speech_recognition import Microphone, Recognizer, UnknownValueError
from pythonosc.udp_client import SimpleUDPClient
from os.path import basename
from keyboard import wait


driver = SimpleUDPClient("127.0.0.1", 9000)
engine = Recognizer()
mic = Microphone()


START_SEQUENCE = "avatar "
DISABLE = "disable "
ENABLE = "enable "


print(f"{basename(__file__)} is now running\n\nbe silent for a moment to set the mic sensitivity\n")
with mic as back_ground_noise: engine.adjust_for_ambient_noise(back_ground_noise, duration=2)
print(f"mic sensitivity set to: {engine.energy_threshold}\n\npress \"F\" to speak!\n")


def voice_command():
    print("listening now...\n")
    with mic as voice: speech = engine.listen(voice)
    try:
        command = str(engine.recognize_google(speech)).casefold()
        print(f"speech recognized as: {command}.\n")
        if START_SEQUENCE and DISABLE in command:
            parameter = command.replace(START_SEQUENCE, "").replace(DISABLE, "").capitalize()
            print(f"disabling the following parameter: {parameter}\n")
            driver.send_message(f"/avatar/parameters/{parameter}", True)
            print("voice-command sent to vrchat!\n")
        elif START_SEQUENCE and ENABLE in command:
            parameter = command.replace(START_SEQUENCE, "").replace(ENABLE, "").capitalize()
            print(f"enabling the following parameter: {parameter}\n")
            driver.send_message(f"/avatar/parameters/{parameter}", False)
            print("voice-command sent to vrchat!\n")
        else:
            print("error: unsupported command!")
        #
    except UnknownValueError:
        print("didn't quite get that, try again...\n\npress \"F\" to speak!\n")
        command = ""
    #
#


while True:
    wait("f")
    voice_command()
#
