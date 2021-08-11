from pathlib import Path
PATH = Path(__file__).parents[2]

def bounds():
    '''Return list of xmin, ymin, xmax, ymax based on config file.
    '''
    from src.utils import config
    
    config = config()
    
    return list(config['region'].values())


def canonical_grid():
    '''Return canonical grid based on config bounds and resolution provided.
    '''
    
    from xarray import Dataset
    from src.utils import config
    from .utils import bounds
    from numpy import arange
    from pathlib import Path
    
    config = config()
    
    res = config['grid']['resolution']
    xmin, ymin, xmax, ymax = bounds()
    
    ds = Dataset(coords={"lon": (['lon'],arange(xmin, xmax+res, res)),
                         "lat": (['lat'],arange(ymin, ymax+res, res))
                        }
                )

    return ds