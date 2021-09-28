from PIL import Image  # Python Image Library - Image Processing
import glob
for file in glob.glob("*.jpeg"):
 img = Image.open(file)
 rgb_img = img.convert('RGB')
 rgb_img.save(file.replace("jpeg", "jpg"), quality=50)