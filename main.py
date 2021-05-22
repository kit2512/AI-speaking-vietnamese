import speech_recognition as sr
from time import strftime
from datetime import date
import pyttsx3
import wikipedia

engine = pyttsx3.init()
r = sr.Recognizer()
robot = ""
while True:


    with sr.Microphone() as source:
        print("Robot: Tôi đang nghe")
        audio_data = r.record(source, duration=5)
    try:
        you = r.recognize_google(audio_data, language="vi")
    except:
        you = ""
    print("you: " + you)

    if "mấy giờ" in you:
        time = strftime("%H: %M:")
        robot = "Bây giờ là " + time
    elif "chào" in you:
        robot = "Xin chào"
    elif "Hôm nay"  in you:
        today = date.today()
        d2 = today.strftime("%d/%m/%Y")
        robot = "Hôm nay là ngày " + d2
    elif "cảm ơn" in you:
        robot = "Không có gì"
    elif "bạn là ai" in you:
        robot = "tôi là con trí tuệ nhân tạo xịn xò nhất hành tinh"
    elif "tạm biệt" in you:
        robot = "Nhớ giữ gìn sức khỏe đấy nhé"
        id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
        engine.setProperty("voice", id)
        engine.say(robot)
        print("Robot: " + robot)
        break
    elif "mệt" in you:
        robot = "Bạn nên nghỉ ngơi"
    elif "đau" in you:
        robot = "cứu cứu cứu cứu cứu"
    elif you:
        wikipedia.set_lang("vi")
        robot = wikipedia.summary(you, sentences=1)
    else:
        robot = "Xin lỗi.Bạn có thể nói lại được không"
    id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MSTTS_V110_viVN_An"
    engine.setProperty("voice", id)
    engine.say(robot)
    print("Robot: " + robot)
    engine.runAndWait()