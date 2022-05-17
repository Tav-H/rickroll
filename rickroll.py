import cv2
import numpy as np
#ffpyplayer for playing audio
from ffpyplayer.player import MediaPlayer
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
	IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

	
video_path="rickroll.mp4"
window_name = 'rick astley'

video=cv2.VideoCapture(video_path)
fps = video.get(cv2.CAP_PROP_FPS)
player = MediaPlayer(video_path)
sleep_ms = int(np.round((1/fps)*1000))
cv2.namedWindow(window_name, cv2.WND_PROP_FULLSCREEN)
cv2.setWindowProperty(window_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
while True:
	grabbed, frame=video.read()
	audio_frame, val = player.get_frame()
	if not grabbed:
		print("End of video")
		break
	if cv2.waitKey(sleep_ms) & 0xFF == ord("q"):
		break
	cv2.imshow(window_name, frame)
	if val != 'eof' and audio_frame is not None:
		#audio
		img, t = audio_frame
	volume.SetMasterVolumeLevel(-0.0, None)
	volume.SetMute(0, None)
video.release()
cv2.destroyAllWindows()
run = False


		

