import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    num = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(num)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("Image taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()



def upload_file(img_name):
    dropbox_access_token= "sl.BCo4PP0JrL_vvemFhTXoGDQoJtXSO_lPS5WKhZwNVi5s5kk05imdU2-3pYtieBgvfm-5wJ9DNllIkrGwvbupffjqqIvLeiV11i4attTTS1zfXLvpytw9t_y16Qw5B-8t6-CBNclNrCo"
    file =img_name
    file_from = file
    file_to="C:/Users/friend/Desktop/python/Class102/" + img_name
    dbx = dropbox.Dopbox(dropbox_access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")


def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()
