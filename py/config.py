# VoicevoxエンジンのURL
BASE_URL = "http://127.0.0.1:50021"
# 保存するディレクトリ
BASE_DIR = "wav/tmp_"


def conversation_script(scripts, speaker1, speaker2):
    """テキストとスピーカで辞書を作成"""
    conversation_script = []
    for i, text in enumerate(scripts.split()):
        speaker = speaker1
        if i % 2 == 1:
            speaker = speaker2
        tmp = {"text": text, "speaker": speaker}
        conversation_script.append(tmp)
    return conversation_script
