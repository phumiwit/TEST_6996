import requests
import json
if __name__ == "__main__":
    url = "https://predict1-gaxsrkp74a-de.a.run.app"
    # test_audio = 'D:\FINALMLAPI\doja.wav'
    # audio_file = open(test_audio,"rb")
    # values = {"file":(test_audio,audio_file,"audio/wav")}
    values = {'file' : "EMINEM.wav"}
    value_t = json.dumps(values)
    resp = requests.post(url=url,data=value_t)
    print(resp.text)