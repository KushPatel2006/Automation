import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.iamwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()


def upload_file(img_name):
    access_token = "sl.BAC3uJz_aniNmfpd6HfX-e0j5TkSh-b52LPjcUghrzN_iQB9wpG2a_DO910rd386ygRGUePCATvby7-oI5QgpQP7LfZAEC4oRiZU_Qd3Kzmnoda70GTbR37mkC_Wn4VEtcFD8E0"
    file = img_name
    file_from = file
    file_to = "/testFolder/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, "rb") as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time()- start_time) >=5):
            name = take_snapshot()
            upload_file(name)

main()
        
