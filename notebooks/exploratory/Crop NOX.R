# library
library(ncdf4)
library(raster)

#load file
ncpath <- "/Users/Paolo/Documents/R/ESoCW/"

ncf_raster <- brick("MAY_HOURLY_2019_NOX.nc", varname="EMISSIONS_2019")
print(ncf_raster)

#Crop W-E-S-N
#We crop a region a little bigger than we need
croparea <- extent(3.9,12.1,42.9,51.1)
ncf_raster_cropped <- crop(ncf_raster,croparea)
print(ncf_raster_cropped)

#Write cropped file
nrc <- writeRaster(ncf_raster_cropped, filename=file.path(ncpath, 'MAY_HOURLY_2019_NOX_reduced.nc'), 
                  overwrite=TRUE, format="CDF",zunit="hours since 2019-05-01 00:00:00",
                  varname="EMISSIONS_2019", xname="longitude", yname="latitude", zname="time")

