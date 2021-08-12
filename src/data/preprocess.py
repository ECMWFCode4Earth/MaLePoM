import xarray as xr
import numpy as np
import pandas as pd
# import rioxarray as rx
import yaml


def rename_dims(da):
    '''Checks dimension names of Dataset of DataArray and standardizes them to 'lat', 'lon'.  
    '''
    
    if ('latitude' in list(da.dims)) and ('longitude' in list(da.dims)):
        da = da.rio.write_crs('epsg:4326')
        da = da.rename({'latitude':'lat', 'longitude':'lon'})

    if ('x' in list(da.dims)) and ('y' in list(da.dims)):
        da = da.rio.write_crs('epsg:4326')
        da = da.rename({'x':'lon', 'y':'lat'})
       
    print('Renamed dims.')
    return da


def clip(da):   
    '''Clip DataArray or Dataset to given region bounds
    '''
    
    from .utils import bounds
    
    xmin, ymin, xmax, ymax = bounds() 
    
    da = rename_dims(da)
    
    if da.lon.values[1] < da.lon.values[0]:
        da = da.sortby('lon', ascending=True)
    
    if da.lat.values[1] < da.lat.values[0]:
        da = da.sortby('lat', ascending=True)
        
#     da = da.sel(lat=slice(ymin, ymax), lon=slice(xmin, xmax))
    
    print('Clipped data.')
    return da


def regrid(da):
    '''Regrid Dataset or DataArray to canonical grid by linear intepolation.
    '''
    
    from .utils import canonical_grid
    from xarray import align
    import os
    
    resolution = yaml.safe_load(open('./config.yml'))['grid']['resolution']
    
    grid = canonical_grid()
   
    da = clip(rename_dims(da))

    if abs(da.lon.values[0] - da.lon.values[1]) == resolution:
        a, b = align(da, grid, join='right')
        da = a
        
    else:
        da = da.interp_like(grid)
        
    return da