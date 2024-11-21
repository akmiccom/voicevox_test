import wave
import numpy as np
import glob


def combine():

    audios = []

    for f in sorted(glob.glob("audio_*.wav")):
        with wave.open(f, "rb") as fp:
            buf = fp.readframes(-1)  # 全フレーム読み込み
            assert fp.getsampwidth() == 2  # と仮定（np.int16でキャスト）
            audios.append(np.frombuffer(buf, np.int16))
            params = fp.getparams()
    audio_data = np.concatenate(audios)

    # 正規化（ピーク時基準）
    scaling_factors = [
        np.iinfo(np.int16).max / (np.max(audio_data) + 1e-8),
        np.iinfo(np.int16).min / (np.min(audio_data) + 1e-8),
    ]

    # s>0:位相が反転しないようにする。ここをmaxにするとプチッというノイズが入るので注意
    scaling_factors = min([s for s in scaling_factors if s > 0])
    audio_data = (audio_data * scaling_factors).astype(np.int16)
    with wave.Wave_write("combine.wav") as fp:
        fp.setparams(params)
        fp.writeframes(audio_data.tobytes())
