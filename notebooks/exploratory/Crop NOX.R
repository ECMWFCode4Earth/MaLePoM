# library
library(ncdf4)
library(raster)

#Folder for the files
ncpath <- "/Users/Paolo/Documents/R/ESoCW/"

#We crop a region a little bigger than we need
#Crop W-E-S-N
croparea <- extent(3.9,12.1,42.9,51.1)

#-------------------------------------------------------------------------------
#MAY_HOURLY_2019_NOX

#Import the file
ncf_raster <- brick("MAY_HOURLY_2019_NOX.nc", varname="EMISSIONS_2019")
print(ncf_raster)

#Crop the file
ncf_raster_cropped <- crop(ncf_raster,croparea)
print(ncf_raster_cropped)

#Write cropped file
nrc <- writeRaster(ncf_raster_cropped, filename=file.path(ncpath, 'MAY_HOURLY_2019_NOX_reduced.nc'), 
                  overwrite=TRUE, format="CDF",zunit="hours since 2019-05-01 00:00:00",
                  varname="EMISSIONS_2019", xname="longitude", yname="latitude", zname="time")

#-------------------------------------------------------------------------------
#MAY_HOURLY_2019_NOX

#Import the file
ncf_raster_MAY_HOURLY_2020_NOX <- brick("MAY_HOURLY_2020_NOX.nc", varname="EMISSIONS_2020")
print(ncf_raster_MAY_HOURLY_2020_NOX)

#Crop the file
ncf_raster_MAY_HOURLY_2020_NOX_cropped <- crop(ncf_raster_MAY_HOURLY_2020_NOX,croparea)
print(ncf_raster_MAY_HOURLY_2020_NOX_cropped)

#Write cropped file
nrc <- writeRaster(ncf_raster_MAY_HOURLY_2020_NOX_cropped, filename=file.path(ncpath, 'MAY_HOURLY_2020_NOX_reduced.nc'), 
                   overwrite=TRUE, format="CDF",zunit="hours since 2020-05-01 00:00:00",
                   varname="EMISSIONS_2019", xname="longitude", yname="latitude", zname="time")

#-------------------------------------------------------------------------------
#JUL_HOURLY_2019_NOX.nc

#Import the file
ncf_raster_JUL_HOURLY_2019_NOX <- brick("JUL_HOURLY_2019_NOX.nc", varname="EMISSIONS_2019")
print(ncf_raster_JUL_HOURLY_2019_NOX)

#Crop the file
ncf_raster_JUL_HOURLY_2019_NOX_cropped <- crop(ncf_raster_JUL_HOURLY_2019_NOX,croparea)
print(ncf_raster_JUL_HOURLY_2019_NOX_cropped)

#Write cropped file
nrc <- writeRaster(ncf_raster_JUL_HOURLY_2019_NOX_cropped, filename=file.path(ncpath, 'JUL_HOURLY_2019_NOX_reduced.nc'), 
                   overwrite=TRUE, format="CDF",zunit="hours since 2019-07-01 00:00:00",
                   varname="EMISSIONS_2019", xname="longitude", yname="latitude", zname="time")




