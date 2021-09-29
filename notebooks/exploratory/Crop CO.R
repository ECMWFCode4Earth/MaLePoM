# library
library(ncdf4)
library(raster)

#Folder for the files
ncpath <- "/Users/Paolo/Documents/R/ESoCW"

#We crop a region a little bigger than we need
#Crop W-E-S-N
croparea <- extent(3.9,12.1,42.9,51.1)

#-------------------------------------------------------------------------------
#MAY_HOURLY_2019_CO.nc

#Import the file
ncf_raster_co <- brick("MAY_HOURLY_2019_CO.nc", varname="EMISSIONS_2019")
print(ncf_raster_co)

#Crop the file
ncf_raster_cropped <- crop(ncf_raster_co,croparea)
print(ncf_raster_cropped)

#Write cropped file
nrc <- writeRaster(ncf_raster_cropped, filename=file.path(ncpath, 'MAY_HOURLY_2019_CO_reduced.nc'), 
                   overwrite=TRUE, format="CDF",zunit="hours since 2019-05-01 00:00:00",
                   varname="EMISSIONS_2019", xname="longitude", yname="latitude", zname="time")

#-------------------------------------------------------------------------------
#MAY_HOURLY_2020_CO.nc

#Import the file
ncf_raster_MAY_HOURLY_2020_CO <- brick("MAY_HOURLY_2020_CO.nc", varname="EMISSIONS_2020")
print(ncf_raster_MAY_HOURLY_2020_CO)

#Crop the file
ncf_raster_MAY_HOURLY_2020_CO_cropped <- crop(ncf_raster_MAY_HOURLY_2020_CO,croparea)
print(ncf_raster_MAY_HOURLY_2020_CO_cropped)

#Write cropped file
nrc <- writeRaster(ncf_raster_MAY_HOURLY_2020_CO_cropped, filename=file.path(ncpath, 'MAY_HOURLY_2020_CO_reduced.nc'), 
                   overwrite=TRUE, format="CDF",zunit="hours since 2020-05-01 00:00:00",
                   varname="EMISSIONS_2020", xname="longitude", yname="latitude", zname="time")

#-------------------------------------------------------------------------------
#JUL_HOURLY_2019_CO.nc

#Import the file
ncf_raster_JUL_HOURLY_2019_CO <- brick("JUL_HOURLY_2019_CO.nc", varname="EMISSIONS_2019")
print(ncf_raster_JUL_HOURLY_2019_CO)

#Crop the file
ncf_raster_JUL_HOURLY_2019_CO_cropped <- crop(ncf_raster_JUL_HOURLY_2019_CO,croparea)
print(ncf_raster_JUL_HOURLY_2019_CO_cropped)

#Write cropped file
nrc <- writeRaster(ncf_raster_JUL_HOURLY_2019_CO_cropped, filename=file.path(ncpath, 'JUL_HOURLY_2019_CO_reduced.nc'), 
                   overwrite=TRUE, format="CDF",zunit="hours since 2019-07-01 00:00:00",
                   varname="EMISSIONS_2019", xname="longitude", yname="latitude", zname="time")






