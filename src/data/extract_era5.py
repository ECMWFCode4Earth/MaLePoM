from pathlib import Path
PATH = Path(__file__).parents[2]
    
def _get_time_from_config():
    '''Convert `start`, `end` and `freq` specified in config.yml to CDS API-readable values.'''
    
    from src.utils import config
    from pandas import to_datetime
    
    config = config()

    start = to_datetime(config['period']['start'])
    end   = to_datetime(config['period']['end'])

    if start.year == end.year:
        years = ['%s'%start.year]
    else:
        years = [str(x) for x in np.arange(start.year,end.year+1).tolist()]
         
    if start.month == end.month:
        months = ['%s'%start.month]
    else:
        months = [str(x) for x in np.arange(start.month,end.month+1).tolist()]

    days = [str(x) for x in np.arange(1,32).tolist()]

    times = ['00:00', '01:00', '02:00', '03:00', '04:00', '05:00', 
             '06:00', '07:00', '08:00', '09:00', '10:00', '11:00', 
             '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', 
             '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']

    return years, months, days, hours


def extract_era5(variables, path=PATH.joinpath('data/raw/')):
    '''Using CDS API to request ERA5 data for variables specified. Variable names can be found at 
    https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=overview . 
    Time period and area will be inferred from the `config.yml` file. 
    ''' 
    
    from src.utils import config, keys
    import _get_time_from_config
    
    config = config()
    keys = keys()
    
    years, months, days, hours = _get_time_from_config()
    
    uri, key = keys['COPERNICUS']['uri'], keys['COPERNICUS']['key']
    
    c = cdsapi.Client(url='https://cds.climate.copernicus.eu/api/v2', key='%s:%s'%(uri, key))
    
    res = c.retrieve("reanalysis-era5-single-levels",  {'product_type': 'reanalysis',
                                                        'variable': variables,
                                                        'year': years,
                                                        'month': months,
                                                        'day':  days,
                                                        'time': times,
                                                        'format': 'netcdf',
                                                        'area'          : [38, 68, 40, 70],
                                                        'grid'          : [0.25, 0.25]
                                                       }
                    )
    
    res.download(path.joinpath(res.location.split('/')[-1]))
    
    return 'Completed.'