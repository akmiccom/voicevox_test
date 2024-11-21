from config import BASE_DIR
from synthesize_voice import synthesize_voice


text = "すみません。この傘はあなたのですか？"
synthesize_voice(text, speaker=29, output_file=f"{BASE_DIR}{1:02}.wav")
