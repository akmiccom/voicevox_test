import requests


def synthesize_voice(text, speaker, output_file):
    """
    Voicevoxを使って音声を生成し、指定したファイルに保存
    :param text: 合成するテキスト
    :param speaker: スピーカーID
    :param output_file: 保存先ファイルパス
    """

    BASE_URL = "http://127.0.0.1:50021"

    # 音声クエリを生成
    response = requests.post(
        f"{BASE_URL}/audio_query", params={"text": text, "speaker": speaker}
    )
    if response.status_code != 200:
        print("クエリ生成に失敗:", response.text)
        return None

    query = response.json()

    # 音声を生成
    response = requests.post(
        f"{BASE_URL}/synthesis", json=query, params={"speaker": speaker}
    )
    if response.status_code != 200:
        print("音声生成に失敗:", response.text)
        return None

    # ファイルに保存
    with open(output_file, "wb") as f:
        f.write(response.content)
    print(f'File Save : {output_file}')

    return output_file


if __name__ == "__main__":

    BASE_DIR = "wav/sample_"
    text = "すみません。この傘はあなたのですか？"
    synthesize_voice(text, speaker=29, output_file=f"{BASE_DIR}{1:02}.wav")
