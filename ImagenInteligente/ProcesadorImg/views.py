from ProcesadorImg.models import ImagenBase
from django.shortcuts import redirect, render
from ProcesadorImg.froms import FormImagen
from django.http import HttpResponse
## DALI

from skimage import data, io
from PIL import Image
import numpy as np
import cv2

## MATRICES
kernel = np.array([
  [-1, -1, -1],
  [-1, 9, -1],
  [-1, -1, -1]
])



kernel = np.array([
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1]
])/9

# LPF = cv2.filter2D(src_image, -1, kernel)
# blur_image = cv2.GaussianBlur(src_image,(5,15),0)

# new_image = src_image - blur_image #HPF

# ima = src_image+new_image
def primer_procesamiento(direcion):
    image= io.imread(direcion) - 100
    im = Image.fromarray(image)
    im.save(".\\media\\images\\filename.jpg")
    
def index(request):
    if request.method == 'POST':
        formulario = FormImagen(request.POST, request.FILES)
        #imagen_p = formulario.cleaned_data['img']
        datos = str(request.POST['title'])
        if datos == "1" :
            direcion = request.FILES['image']
            primer_procesamiento(direcion)
        if datos == "2" :
            print("Ecualción 2")
        if datos == "3" :
            print("Ecualción 3")
        if datos == "4" :
            print("Ecualción 4")
        if datos == "5" :
            print("Ecualción 5")
        if formulario.is_valid() :
            formulario.save()
            img_obj = formulario.instance
            return render(request,'index.html',{'formulario':formulario, 'img_obj':img_obj})
    else:
        formulario = FormImagen()

    return render(request,'index.html',{'formulario':formulario})

def respuesta(request):
    respuesta = ' index. <img src="./filename.jpeg" alt="Girl in a jacket" width="500" ">'
    return render(request,'resp.html',{'formulario':'formulario'})