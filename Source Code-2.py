import cv2 
import mediapipe as mpimport 
pyautogui import 
random import util 
frompynput.mouseimportButton, 
Controller mouse = Controller() 
Screen_width,screen_height=pyautogui.size() 
mpHands = mp.solutions.hands 
hands = mpHands.Hands( static_image_mode=False, model_complexity=1, 
min_detection_confidence=0.7,min_tracking_confidence=0.7,max_num_hands=1) 
def find_finger_tip(processed): 
if processed.multi_hand_landmarks: 
hand_landmarks=processed.multi_hand_landmarks[0] 
# Assuming only one hand is detected 
index_finger_tip= 
 hand_landmarks.landmark[mpHands.HandLandmark.INDEX_FINGER_TIP] 
return index_finger_tipreturn None, None 
def move_mouse(index_finger_tip): 
ifindex_finger_tipisnot None: 
x=int(index_finger_tip.x*screen_width)y=int(index_finger_tip.y/2*screen_height) 
pyautogui.moveTo(x, y) 
t_click(landmark_list,thumb_index_dist): 
return(util.get_angle(landmark_list[5],landmark_list[6],landmark_list[8])<50and 
util.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) > 90 and 
thumb_index_dist> 50) 
defis_right_click(landmark_list,thumb_index_dist): 
return(util.get_angle(landmark_list[9],landmark_list[10],landmark_list[12])<50
and util.get_angle(landmark_list[5],landmark_list[6],landmark_list[8])>90and 
thumb_index_dist> 50) 
Def is_double_click(landmark_list,thumb_index_dist): 
return(util.get_angle(landmark_list[5],landmark_list[6],landmark_list[8])<50and 
util.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and 
thumb_index_dist> 50) 
defis_screenshot(landmark_list,thumb_index_dist): 
return(util.get_angle(landmark_list[5],landmark_list[6],landmark_list[8])<50and 
util.get_angle(landmark_list[9], landmark_list[10], landmark_list[12]) < 50 and 
thumb_index_dist< 50 ) 
defdetect_gesture(frame,landmark_list,processed): 
iflen(landmark_list)>=21: 
index_finger_tip=find_finger_tip(processed) 
thumb_index_dist=util.get_distance([landmark_list[4],landmark_list[5]]) if 
util.get_distance([landmark_list[4], landmark_list[5]]) < 50 and 
util.get_angle(landmark_list[5], landmark_list[6], landmark_list[8]) > 90: 
move_mouse(index_finger_tip) 
elifis_left_click(landmark_list,thumb_index_dist): 
mouse.press(Button.left)mouse.release(Button.left) 
cv2.putText(frame,"LeftClick",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1, 
(0,255,0),2) 
elifis_right_click(landmark_list,thumb_index_dist): 
mouse.press(Button.right) 
mouse.release(Button.right) 
cv2.putText(frame,"RightClick",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1, 
 (0,0,255),2) 
elifis_double_click(landmark_list,thumb_index_dist):
pyautogui.doubleClick()cv2.putText(frame,"DoubleClick",(50,50), 
cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2) 
elifis_screenshot(landmark_list,thumb_index_dist): 
im1 = pyautogui.screenshot() 
label=random.randint(1,1000) 
im1.save(f'my_screenshot_{label}.png') 
cv2.putText(frame,"ScreenshotTaken",(50,50),cv2.FONT_HERSHEY_SIMPLEX,1, 
(255,255,0), 2) 
def main(): 
draw=mp.solutions.drawing_utils 
cap = cv2.VideoCapture(0) 
try: 
while cap.isOpened(): 
ret,frame=cap.read()ifnotret:break 
 frame = cv2.flip(frame, 1) 
frameRGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) 
 processed = hands.process(frameRGB) 
landmark_list= [] 
if processed.multi_hand_landmarks: 
hand_landmarks=processed.multi_hand_landmarks[0] 
# Assuming only one hand is detected 
draw.draw_landmarks(frame,hand_landmarks,mpHands.HAND_CONNECTIONS) 
for lm in hand_landmarks.landmark: 
landmark_list.append((lm.x, lm.y)) 
detect_gesture(frame,landmark_list,processed) 
cv2.imshow('Frame', frame) 
ifcv2.waitKey(1)&0xFF==ord('q'):breakfinally: 
cap.release() cv2.destroyAllWindows()
if name ==' main ': 
main() 
import numpy as np 
def get_angle(a,b,c): 
radians=np.arctan2(c[1]-b[1],c[0]-b[0])-np.arctan2(a[1] -b[1],a[0]-b[0]) angle = 
np.abs(np.degrees(radians)) return angle 
def get_distance(landmark_ist): 
if len(landmark_ist)< 2: 
return 
(x1,y1),(x2,y2)=landmark_ist[0],landmark_ist[1] 
L=np.hypot(x2 -x1,y2-y1)returnnp.interp(L,[0,1],[0,1000]
