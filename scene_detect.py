import cv2
import numpy as np
import PIL
import io
import html
import time
from IPython.display import display, Javascript, Image
from google.colab.output import eval_js
from google.colab.patches import cv2_imshow
from base64 import b64decode, b64encode
from matplotlib import pyplot as plt



uda.ge!git clone https://github.com/ultralytics/yolov5 # clone repo
%pip install -qr requirements.txt # install dependencies
%pip install -q roboflow

import torch
import os
from IPython.display import Image, clear_output  # to display images

print(f"Setup complete. Using torch {torch.__version__} ({torch.ct_device_properties(0).name if torch.cuda.is_available() else 'CPU'})")



!unzip "/content/drive/MyDrive/data.zip"


import shutil
for src in ['train', 'test', 'valid']:
    os.makedirs(f"/content/data/{src}/images/", exist_ok=True)
    os.makedirs(f"/content/data/{src}/labels/", exist_ok=True)
    files = os.listdir(f"/content/{src}/images")
    for f in files:
        shutil.copy(f"/content/{src}/images/{f}", f"/content/data/{src}/images/{f}")
        
    files = os.listdir(f"/content/{src}/labels")
    for f in files:
        shutil.copy(f"/content/{src}/labels/{f}", f"/content/data/{src}/labels/{f}")
        
        
  !python "yolov5/train.py" --img 416 --batch 16 --epochs 4 --data "/content/data.yaml" --weights yolov5x.pt --cache
  
  
  !python "yolov5/val.py" --task test --weights yolov5/runs/train/exp/weights/best.pt --data /content/data.yaml
  
  
  
  !python "yolov5/detect.py" --weights yolov5x.pt --data 0523b641cddd9cbb.jpg
  
  
  
  
  model = torch.hub.load('ultralytics/yolov5', 'custom', path='/content/yolov5/runs/train/exp/weights/best.pt', force_reload=True)
  
  
  
  
##model = torch.hub.load('ultralytics/yolov5', 'yolov5x')  

model


from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode

def take_photo(filename='photo.jpg', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // Wait for Capture to be clicked.
      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename
  
  
  
  from IPython.display import Image
try:
  filename = take_photo()
  print('Saved to {}'.format(filename))
  
  # Show the image which was just taken.
  display(Image(filename))
except Exception as err:
  # Errors will be thrown if the user does not have a webcam or if they do not
  # grant the page permission to access it.
  print(str(err))
  
  
  
  img = "/content/photo.jpg"
  
  results = model(img)
results.print()

%matplotlib inline 
plt.imshow(np.squeeze(results.render()))
plt.show()
