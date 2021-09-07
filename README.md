MaLePoM
================

MaLePoM (Machine Learning for Pollution Monitoring) is part of ECMWF's European Summer of Weather Code 2021 event. Through this project we aim to improve the spatial and temporal accuracy of emissions estimates for NOx by constructing a machine learning model using suitable proxy data. 

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


Background
--------
#### Datasets used
|           Dataset          |                  Source                 | Spatial resolution | Temporal resolution | Notes                                                                                                             |
|:--------------------------:|:---------------------------------------:|:------------------:|:-------------------:|-------------------------------------------------------------------------------------------------------------------|
| Land-use/land cover (LULC) | Copernicus Land Monitoring Service 2018 |        100m        |         n/a         |                                                                                                                   |
| Real-time traffic data     | HERE Traffic API                        |         n/a        |         n/a         | Traffic data is available in real-time via the API. Data is gathered and stored using the API at several times.   |
| Meteorological variables   | ERA5 reanalysis                         |    0.25 degrees    |        1 hour       | Temperature, wind speed, precipitation, humidity, and cloud cover are obtained from the ERA5 reanalysis dataset   |
| Atmospheric concentrations | CAMS global reanalysis                  |        ~80km       |       3 hours       | Surface concentrations of NO, NO2, CO, CO2, CH4, and O3 are obtained from the CAMS Global Reanalysis product      |                                                                                                |


Using this code
--------

#### 1. Clone repository
Run `git clone https://github.com/esowc/MaLePoM.git`

#### 2. Create local `api_keys.yml` to store private API keys
API keys are used to access various datasets, and their keys are stored in a private yaml file as described below. Copy-paste the below into a new text file, add the API keys, and rename the file to `api_keys.yaml`.

    HERE:
        key: #######

    COPERNICUS:
        uri: #####
        key: ############

    WEKEO:
        username: #########
        password: #########

    FTP_SERVER:
        username: #########
        password: #########
