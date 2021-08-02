'''
This is the main class which, given an input file (.nc, .tar.gz or .zip), it creates the xarray dataset.
PAY ATTENTION:
- The file MUST be netcdf file, it can be compressed into zip or tar.gz but it has to be netcdf inside!!
- File cannot contain ".tar.gz" or ".zip" inside the name, jsut at the end

'''

# importing required modules
from zipfile import ZipFile
import tarfile
import xarray as xr
import numpy as np


class CustomDataset:
	
  def __init__(self, filename):
    self.filename = filename
    self.decompress()

  def decompress(self):
    if self.filename.endswith("tar.gz"):
      tar = tarfile.open(fname, "r:gz")
      print('Extracting all the files now...')
      tar.extractall()
      tar.close()
      print('Done!')
      self.filename = self.filename.replace("tar.gz", "nc")
    elif self.filename.endswith(".zip"):
      # opening the zip file in READ mode
      with ZipFile(file_name, 'r') as zip:  
        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall()
        print('Done!')
        self.filename = self.filename.replace("zip", "nc")
    self.open_dataset()

  def set_filename(self, filename):
    self.filename = filename

  def open_dataset(self):
    print("Opening dataset at : ", self.filename)
    self.dataset = xr.open_dataset(self.filename)
    print("Done!")

  def rescale(self, target_res = 0.25, method = 'nearest'):

    assert ('latitude' in self.dataset.variables),"latitude column missing (name must be 'latitude')"
    assert ('longitude' in self.dataset.variables),"longitude column missing (name must be 'longitude')"

    #da = data.to_array()

    lats = self.dataset.latitude.values
    longs = self.dataset.longitude.values

    lats.sort()
    longs.sort()

    #lats_res = round(abs(lats[1] - lats[0]), 2) # supposing at least 2 values and max_precision = 2 decimals and res_lat = res_long
    #lat_interval = abs(round(lats[-1],2) - round(lats[0], 2))
    #long_interval = abs(round(longs[-1],2) - round(longs[0], 2))
    lat_interval = np.float32(lats[-1] - lats[0])
    long_interval = np.float32(longs[-1] - longs[0])
    #print("lat interval is ",lat_interval)
    #print("long interval is --> " , long_interval)
    lat_new_squares = lat_interval // target_res
    #print(lat_new_squares)
    long_new_squares = long_interval // target_res
    #print(long_new_squares)
    new_lat_values= np.around(np.arange(0, lat_new_squares +1 , 1) * target_res + round(lats[0], 2), decimals=2)
    #print("New latitude values are -> ", new_lat_values)
    new_long_values= np.around(np.arange(0, long_new_squares +1 , 1) * target_res + round(longs[0], 2), decimals=2)
    #print("New longitude values are -> ", new_long_values)
    #da = da.sortby(['latitude','longitude','time'])
    #df_temp = data.interp(latitude = new_lat_values, longitude = new_long_values, method = method)
    #df= df_temp.interp(longitude = new_long_values, method = method)

    return self.dataset.interp(latitude = new_lat_values, longitude = new_long_values, method = method)

  def get_dataset(self):
    return self.dataset

