import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("음성 인식 중입니다. 말씀하세요...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("음성을 인식하는 중...")
        speech_text = recognizer.recognize_google(audio, language="ko-KR")
        print(f"인식된 음성: {speech_text}")
        return speech_text
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다.")
        return None
    except sr.RequestError:
        print("음성 인식 서비스에 접근할 수 없습니다.")
        return None
