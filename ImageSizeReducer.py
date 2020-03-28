import cv2
import os
import numpy as np

class ImageSizeReducer:
  def __init__(self, width=800, height=500, jpg_quality=30):
    self.output_path = ""
    self.input_path = ""
    self.dim = (width, height)
    self.jpg_quality = jpg_quality
    self.num_compressed_image = 0

  def check_path(self, path):
    if os.path.isdir(path):
      return path
    else:
      raise UserWarning("Enter a valid directory path ... {}   isn't valid".format(path))

  def __set_output_path(self, input_path):

    self.output_path =  os.path.join(input_path, "Output")
  
    if not os.path.exists(self.output_path):
      os.mkdir(self.output_path)

  def set_input_path(self, input_path):
    self.input_path = self.check_path(input_path)
    self.__set_output_path(self.input_path)
  
  def set_dim(self, width, height):
    self.dim = (width, height)

  def set_jpg_quality(self, jpg_quality):
    #jpg_quality {int} -- 0 - 100 (higher means better). (default: {30})
    self.jpg_quality = jpg_quality

  def read_image_unicode(self, path):
    return cv2.imdecode(np.fromfile(path, dtype=np.uint8), cv2.IMREAD_UNCHANGED)

  def write_image_unicode(self, path, img):
    """Since OpenCV Support only Ascii, To write Unicode Image
    we can first encode the image in OpenCV format to one dimension numpy ndarray format.
    Then we convert this numpy ndarray to image on disk with the tofile() method.
    """
    _ , im_buf_arr = cv2.imencode(".jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), self.jpg_quality])
    im_buf_arr.tofile(path)

  def save(self, path, image):
    """resize and save given image
    
    Arguments:
        path {string} -- [path to output folder]
        image  -- image to save

    Keyword Arguments:
        jpg_quality {int} -- 0 - 100 (higher means better). (default: {50})
    """
    print("test  ", path)
    resized = cv2.resize(image, self.dim, interpolation = cv2.INTER_AREA)
    self.write_image_unicode(path, resized)
    print("{} is added successfully \n ".format( path))

  def get_num_compressed_image(self):
    return self.num_compressed_image

  def folder_reader(self):
    """read all (JPG,JPEG,PNG) pictures exists in input_path
    """
    self.num_compressed_image = 0 
    for f in os.listdir(self.input_path):
      if f.endswith((".JPG", ".jpeg", ".png", ".jpg")):
          file_path = os.path.join(self.input_path, f)

          name = self.name_without_ext(f)
          ext = ".JPG"
          full_name = name + ext
          self.save(path= os.path.join(self.output_path, full_name ), image= self.read_image_unicode(file_path))
          self.num_compressed_image += 1

  def get_status(self): #whether transfer completed sucsessfully or not
    if (self.num_compressed_image > 0 ):
      return True
    else:
      return False
  
  def name_without_ext(self, file_name):
    """seperates name and extension

    Returns:
        [string] -- name without extension 
    Example:
      Input: Bshr.png --> Returns: Bshr
    """
    return file_name.split(sep=".")[0]

  def resizeAndPad(img, size):
    """returns a compressed/stretched image with respect to its original aspect ratio

    Returns:
        [image] -- scaled image

    Example: 
      Input: imageOriginal --> Retunrs: imageScaled

    """

    h, w = img.shape[:2]
    sh, sw = size

    # interpolation method
    if h > sh or w > sw: # shrinking image
        interp = cv2.INTER_AREA
    else: # stretching image
        interp = cv2.INTER_CUBIC

    # aspect ratio of image
    aspect = w/h  # if on Python 2, you might need to cast as a float: float(w)/h

    # compute scaling and pad sizing
    if aspect > 1: # horizontal image
        new_w = sw
        new_h = np.round(new_w/aspect).astype(int)
    elif aspect < 1: # vertical image
        new_h = sh
        new_w = np.round(new_h*aspect).astype(int)
    else: # square image
        new_h, new_w = sh, sw

    # scale and pad
    scaled_img = cv2.resize(img, (new_w, new_h), interpolation=interp)

    return scaled_img

  def run(self):
    self.folder_reader()
    return self.get_status()