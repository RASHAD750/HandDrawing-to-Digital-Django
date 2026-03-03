from django.shortcuts import render
from django.http import HttpResponseRedirect
import MySQLdb
import matplotlib.pyplot as plt 
from django.core.files.storage import FileSystemStorage
import cv2 
import numpy as np
import os
import numpy as np
import cv2
import natsort
import xlwt
from skimage import exposure
from .models import *
from django.contrib.auth import authenticate
from imageapp.sceneRadianceCLAHE import RecoverCLAHE
from imageapp.sceneRadianceHE import RecoverHE
# Create your views here.
def login(request):
    if(request.POST):
        uname=request.POST.get("uname")
        password=request.POST.get("pass")
        request.session["uname"]=uname
        user=authenticate(username=uname,password=password)
        # s="select role from login where uname='"+uname+"' and pass='"+password+"'"
        # c.execute(s)
        # data=c.fetchone()
        # if(data[0]=="Admin"):
        if(user.userType =="Admin"):
            return HttpResponseRedirect("/adminviewfeedback")
        # elif(data[0]=="User"):
        elif(user.userType =="User"):
            return HttpResponseRedirect("/useraddimage")

    return render(request,"login.html")
def registration(request):
    if(request.POST):
        name=request.POST.get("uname")
        email=request.POST.get("email")
        phone=request.POST.get("phone")
        gen=request.POST.get("gen")
        uname=request.POST.get("uname")
        passw=request.POST.get("pass")
        utype="User"
        obj=Registration.objects.create(name=name,email=email,phone=phone,gender=gen,uname=uname)
        obj.save()
        cus=CustomUser.objects.create_user(username=uname,password=passw,userType=utype,viewpassword=passw)
        cus.save()
        # s="insert into registration (name,email,phone,gender,uname) values('"+name+"','"+email+"','"+phone+"','"+gen+"','"+uname+"')"
        # c.execute(s)
        # con.commit()
        # s1="insert into login values('"+uname+"','"+passw+"','"+utype+"')"
        # c.execute(s1)
        # con.commit()
    return render(request,"userregistration.html")
################ END COMMON PAGE###############

##############ADMIN PAGES##################
def adminviewusers(request):
    # s="select * from registration"
    # c.execute(s)
    # data=c.fetchall()
    data=Registration.objects.all()
    return render(request,"adminviewusers.html",{"data":data})
def adminviewfeedback(request):
    # s="select * from feedback"
    # c.execute(s)
    # data=c.fetchall()
    data=Feedback.objects.all()
    return render(request,"adminviewfeedback.html",{"data":data})


############## END ADMIN PAGES##################

##############User PAGES##################

def useraddimage(request):
    if request.POST :
        name=request.POST.get("name")
        cat=request.POST.get("cat")
        dis=request.POST.get("dis")
        img=request.FILES["img"]
        # filename=request.FILES.get("img")
        # fs=FileSystemStorage('imageapp/static/media')
        # name=fs.save(filename.name,filename)
        # url=fs.url(name)
        # ff="static/media/"+str(filename)
        # s="insert into uploadimage (name,cat,dis,`image`) values('"+str(name)+"','"+str(cat)+"','"+str(dis)+"','"+str(ff)+"')"
        # c.execute(s)
        # con.commit()
        obj=Uploadimage.objects.create(name=name,cat=cat,dis=dis,image=img)
        obj.save()
    return render(request,"useraddimage.html")    
def userviewgalary(request):
    # s="select * from uploadimage"
    # c.execute(s)
    # data=c.fetchall()
    data=Uploadimage.objects.all()
    return render(request,"userviewgalary.html",{"data":data})

def imageenhances(request):
    if request.POST :
        # name=request.POST.get("name")
        # cat=request.POST.get("cat")
        # dis=request.POST.get("dis")
        # filename=request.FILES.get("img")
        # fs=FileSystemStorage('imageapp/static/media')
        # name=fs.save(filename.name,filename)
        # url=fs.url(name)
        # ff="static/media/"+str(filename)
        # s="insert into uploadimage (name,cat,dis,`image`) values('"+str(name)+"','"+str(cat)+"','"+str(dis)+"','"+str(ff)+"')"
        # c.execute(s)
        # con.commit()
        import cv2
        import numpy as np
        name=request.POST.get("name")
        cat=request.POST.get("cat")
        dis=request.POST.get("dis")
        img=request.FILES["img"]
        obj=Uploadimage.objects.create(name=name,cat=cat,dis=dis,image=img)
        obj.save()
        np.seterr(over='ignore')
        
        # folder = "C:/Users/Administrator/Desktop/UnderwaterImageEnhancement/HE"
        folder = "E:/Handdrawing to digital/imageapp/static/media"
        # folder = "C:/Users/Administrator/Desktop/Databases/Dataset"

        # folder = "C:/Users/Administrator/Desktop/UnderwaterImageEnhancement/HE"
        folder = "E:/Handdrawing to digital/imageapp/static/media"
        # folder = "C:/Users/Administrator/Desktop/Databases/Dataset"
       
        filename=img.name
        # Load hand-drawn image
        filepath =str(folder) + "/" + str(filename)
        hand_drawn_image = cv2.imread(filepath)



        # Convert to grayscale
        gray_image = cv2.cvtColor(hand_drawn_image, cv2.COLOR_BGR2GRAY)

        # Smooth the image to reduce noise
        smoothed_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

        # Apply adaptive thresholding to create a binary image
        binary_image = cv2.adaptiveThreshold(smoothed_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 4)

        # Find contours of the objects in the binary image
        contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # Create a mask for filled contours
        filled_contour_mask = np.zeros_like(gray_image)

        # Draw filled contours on the mask
        cv2.drawContours(filled_contour_mask, contours, -1, (255), thickness=cv2.FILLED)

        # Invert the filled contour mask
        filled_contour_mask = cv2.bitwise_not(filled_contour_mask)

        # Combine the filled contour mask with the original hand-drawn image to preserve color
        reconstructed_image = cv2.bitwise_and(hand_drawn_image, hand_drawn_image, mask=filled_contour_mask)

        # Display the reconstructed image
        cv2.imshow('Orginal Image', hand_drawn_image)
        cv2.imshow('Reconstructed Image', reconstructed_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


        # files=filename
        # print('********    file   ********',files)
        # filepath =str(folder) + "/" + str(files)
        

        # # Load the hand-drawn image
        # image_path =filepath 
        # hand_drawing = cv2.imread(image_path)
        # if hand_drawing is None:
        #     print("Error: Unable to load the image.")
        # # Convert the image to grayscale
        # gray_image = cv2.cvtColor(hand_drawing, cv2.COLOR_BGR2GRAY)

        # # Apply thresholding to create a binary image
        # _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

        # # Save the digital image
        # output_path = folder+'/image.jpg'
        # cv2.imwrite(output_path, binary_image)

        # # Display the original and digital images
        # cv2.imshow('Original Image', hand_drawing)
        # cv2.imshow('Digital Image', binary_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

        # filepath=output_path
        # # prefix = files.split('.')[0]
        # if os.path.isfile(filepath):
        #     print('********    file   ********',files)
        #     # img = cv2.imread('InputImages/' + file)
        #     img = cv2.imread(str(folder) +"/"+ str(files))
        #     sceneRadiance = RecoverCLAHE(img)
        #     #cv2.imwrite('OutputImages/' + prefix + '_CLAHE.jpg', sceneRadiance)
        #     cv2.imwrite(str(folder) +"/"+ str(files), sceneRadiance)
            
    return render(request,"useraddimageforenhance.html")    
def imageresize(request):
    image = cv2.imread("C://gfg//tomatoes.jpg", 1) 
# Loading the image 
  
    half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1) 
    bigger = cv2.resize(image, (1050, 1610)) 
    
    stretch_near = cv2.resize(image, (780, 540),  
                interpolation = cv2.INTER_NEAREST) 
    
    
    Titles =["Original", "Half", "Bigger", "Interpolation Nearest"] 
    images =[image, half, bigger, stretch_near] 
    count = 4
    
    for i in range(count): 
        plt.subplot(2, 2, i + 1) 
        plt.title(Titles[i]) 
        plt.imshow(images[i]) 
    
    plt.show() 
    return render(request,"resize.html")
def feedback(request):
    if request.POST :
        feedback=request.POST.get("feedback")
        uname=request.session["uname"]
        # s="insert into uploadimage (feedback,uname) values('"+str(feedback)+"','"+str(uname)+"')"
        # c.execute(s)
        # con.commit()
        obj=Feedback.objects.create(feedback=feedback,uname=uname)
        obj.save()
    return render(request,"Addfeedback.html")  
def resizeimage(request):
    # ss="select * from uploadimage"
    # c.execute(ss)
    # data=c.fetchall()
    data=Uploadimage.objects.all()
    return render(request,"resizeimage.html",{"data":data})  
def resize(request):
    id=request.GET.get("id")
    # ss="select * from uploadimage where id='"+str(id)+"'"
    # c.execute(ss)
    # data=c.fetchall()
    data=Uploadimage.objects.get(id=id)
    if request.POST :
        folder = "D:/image enhance/imageapp/static/media/"+data[0][4]
        image=cv2.imread(folder)
        half = cv2.resize(image, (0, 0), fx = 0.1, fy = 0.1) 
        bigger = cv2.resize(image, (1050, 1610)) 
        
        stretch_near = cv2.resize(image, (780, 540),  
                    interpolation = cv2.INTER_NEAREST) 
        
        
        Titles =["Original", "Half", "Bigger", "Interpolation Nearest"] 
        images =[image, half, bigger, stretch_near] 
        count = 4
        
        for i in range(count): 
            plt.subplot(2, 2, i + 1) 
            plt.title(Titles[i]) 
            plt.imshow(images[i]) 
        
        plt.show() 
    return render(request,"resize.html",{"data":data})  
def changeformat(request):
    id=request.GET.get("id")
    # ss="select * from uploadimage where id='"+str(id)+"'"
    # c.execute(ss)
    # data=c.fetchall()
    data=Uploadimage.objects.get(id=id)
    if request.POST :
        folder = "D:/image enhance/imageapp/static/media/"+data[0][4]
        image=cv2.imread(folder)
        formats=request.POST.get("format")
        filename=str(id)+str(formats)
        path="/static/media"+str(filename)
        cv2.imwrite("D:/image enhance/imageapp/static/media/"+str(filename), img)
        # s="insert into uploadimage (name,cat,dis,`image`) values('"+str(filename)+"','resize','resize','"+str(path)+"')"
        # c.execute(s)
        # con.commit() 

       
    return render(request,"changeformat.html",{"data":data}) 
############## END User PAGES##################