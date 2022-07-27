# 王晗东
# 开发时间 2022/7/15 14:25
import numpy as np
import cv2
import time
#测试usb摄像头并保存一段时长20秒视频

def test():
    cap =  cv2.VideoCapture(1)
    # 视频每秒传输帧数
    fps = cap.get(cv2.CAP_PROP_FPS)
    # 视频图像的宽度
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # 视频图像的长度
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    print(fps,frame_width,frame_height)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('usbuvcvideo.avi',fourcc,fps,(frame_width,frame_height))
    #开始的时间
    time_start = time.time()
    print(time_start)
    while(cap.isOpened()):
        time_now = time.time()
        ret,frame = cap.read()
        cv2.imshow("test",frame)
        out.write(frame)
        print(time_now)
        if(int(time_now-time_start)==10):
            print("save video finish!")
            break
        if (cv2.waitKey(1)==27):
            break
    cap.release()
    out.release()
#    cv2.destoryAllWindows()
    print(cap.isOpened())

if __name__ == '__main__':
    test()
