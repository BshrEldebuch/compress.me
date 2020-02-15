import cv2
import os

class ImageSizeReducer:
  def __init__(self, width=800, height=500, jpg_quality=30):
    self.output_path = ""
    self.input_path = ""
    self.dim = (width, height)
    self.jpg_quality = jpg_quality

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

  def save(self, path, image):
    """resize and save given image
    
    Arguments:
        path {string} -- [path to output folder]
        image  -- image to save

    Keyword Arguments:
        jpg_quality {int} -- 0 - 100 (higher means better). (default: {50})
    """
    resized = cv2.resize(image, self.dim, interpolation = cv2.INTER_AREA)
    cv2.imwrite(path, resized, [int(cv2.IMWRITE_JPEG_QUALITY), self.jpg_quality])
    print("{} is added successfully \n ".format( path))

  def folder_reader(self):
    """read all (JPG,JPEG,PNG) pictures exists in input_path
    """
    self.sucsess = False
    for f in os.listdir(self.input_path):
      if f.endswith((".JPG", ".jpeg", ".png", ".jpg")):
          file_path = os.path.join(self.input_path, f)

          name = self.name_without_ext(f)
          ext = ".JPG"
          full_name = name + ext
          self.save(path= os.path.join(self.output_path, full_name ), image= cv2.imread(file_path))
          self.sucsess = True
    
  def get_status(self): #whether transfer completed sucsessfully or not
    return self.sucsess

  def name_without_ext(self, file_name):
    """seperates name and extension

    Returns:
        [string] -- name without extension 
    Example:
      Input: Bshr.png --> Returns: Bshr
    """
    return file_name.split(sep=".")[0]

  def run(self):
    self.folder_reader()
    return self.get_status()