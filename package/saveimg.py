import cv2

#Save img from url 
class Save_img():
    #
    def __init__(self,url_img):
        self.url_img = url_img


    def save(url_img):
        cap = cv2.VideoCapture(url_img)
        if( cap.isOpened() ) :
            ret,img = cap.read()
            
        #extraer nombre img
        jpg = url_img.find('.jpg')
        for i in range (jpg,0,-1):
            if url_img[i] == '/':
                img_name = url_img[i+1:jpg]+'.jpg'
                # print(img_name+'.jpg')
                break
    
        path = 'resource/unprocessed/'+img_name
        cv2.imwrite(path,img)
        return (img_name, img_name)
