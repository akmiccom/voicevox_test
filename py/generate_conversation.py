from synthesize_voice import synthesize_voice
from config import conversation_script
from pydub import AudioSegment
import os


def generate_conversation(
        conversation_script, output_file="wav/conversation.wav"):
    """
    会話のスクリプトを基に音声を生成し、1つの音声ファイルにまとめる
    :param conversation_script: 会話スクリプト (リスト形式)
    :param output_file: 保存する最終的な音声ファイル
    """
    # 各セリフの音声を生成
    audio_segments = []
    for i, line in enumerate(conversation_script):
        text = line["text"]
        speaker = line["speaker"]
        tmp_file = f"../wav/tmp_{i+1:02}.wav"
        synthesize_voice(text, speaker, tmp_file)
        segment = AudioSegment.from_file(tmp_file)
        audio_segments.append(segment)
        os.remove(tmp_file)

    # 全ての音声を結合
    # combined_audio = sum(audio_segments)
    silence = AudioSegment.silent(duration=500)  # 0.5秒の無音
    combined_audio = sum([segment + silence for segment in audio_segments])

    # ファイルに保存
    combined_audio.export(output_file, format="wav")
    print(f"会話音声を保存しました: {output_file}")


if __name__ == "__main__":

    scripts = """
    すみません。この傘はあなたのですか？/nいえ、違います。
    本当ですか？
    はい、本当です。
    その傘は茶色で、私の傘は黄色ですから。
    """

    speaker1 = 29
    speaker2 = 58

    output_filename = "../wav/conversation.wav"

    generate_conversation(
        conversation_script(scripts, speaker1, speaker2), output_filename
    )
