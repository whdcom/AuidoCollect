# 王晗东
# 开发时间 2022/7/21 15:35
'''
在window下安装pyaudio库
    pip install pyaudio
可能需要修改设备索引号input_device_index(已解决)
之后直接运行进行录音
    python CollectAudio.py
'''
import pyaudio
import wave
import time
#根据设备配置号流信息
CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 30
now = time.localtime()
filename = time.strftime("%Y%m%d%H%M%S")
WAVE_OUTPUT_FILENAME = str(filename)+'.wav'
#生成pyaudio对象
p = pyaudio.PyAudio()
#查找输入设备的索引号
# print(p)
for i in range(p.get_device_count()):
    # print(p.get_device_info_by_index(i))
    if(str(p.get_device_info_by_index(i)).find("PnP Sound Device")!=-1):
        devicenum = i
        print(devicenum)
        break;

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                input_device_index=devicenum,
                frames_per_buffer=CHUNK)

print("* begin recording")

frames = []
#表示每秒要写入多少个块，一个块大小有1024帧
#print(RATE / CHUNK * RECORD_SECONDS)
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()