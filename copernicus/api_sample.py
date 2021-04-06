import cdsapi

c = cdsapi.Client()

c.retrieve(
    'sis-ecv-cmip5-bias-corrected',
    {
        'format': 'zip',
        'variable': 'precipitation_flux',
        'model': 'gfdl_esm2m',
        'experiment': 'rcp_8_5',
        'period': [
            '19510101-19551231', '19560101-19601231', '19610101-19651231',
            '19660101-19701231', '19710101-19751231', '19760101-19801231',
            '19810101-19851231', '19860101-19901231', '19910101-19951231',
            '19960101-20001231', '20060101-20101231', '20210101-20251231',
        ],
    },
    'download.zip')