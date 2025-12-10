from machine import Pin, PWM
import time

# 蜂鳴器設定（接在 GPIO5）
buzzer = PWM(Pin(16))
buzzer.duty(512)  # 50% duty cycle（可調整音量）

# 音符頻率表（Hz）
notes = {
    'C4': 262,
    'D4': 294,
    'E4': 330,
    'F4': 349,
    'G4': 392,
    'A4': 440,
    'B4': 494,
    'C5': 523,
    'D5': 587,
    'E5': 659,
    'F5': 698,
    'G5': 784,
    'Bb4': 466,
}

# 生日快樂歌旋律：(音符名, 時間秒)
melody = [
    ('G4', 0.4), ('G4', 0.4), ('A4', 0.8), ('G4', 0.8), ('C5', 0.8), ('B4', 0.8),
    ('G4', 0.4), ('G4', 0.4), ('A4', 0.8), ('G4', 0.8), ('D5', 0.8), ('C5', 0.8),
    ('G4', 0.4), ('G4', 0.4), ('G5', 0.8), ('E5', 0.4), ('C5', 0.4), ('B4', 0.8), ('A4', 0.8),
    ('F5', 0.4), ('F5', 0.4), ('E5', 0.8), ('C5', 0.4), ('D5', 0.4), ('C5', 0.8),
]

# 播放旋律
for note, duration in melody:
    freq = notes[note]
    buzzer.freq(freq)
    time.sleep(duration)

# 關閉蜂鳴器（停止聲音）
buzzer.duty(0)
