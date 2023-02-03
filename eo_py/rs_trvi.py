import rasterio
from rasterio.windows import Window

# Open the TIFF file
with rasterio.open("20221009_042654_SN21_L1_SR_MS_0.tif") as src:
    # Create windows for each band
    nir_window = Window(col_off=0, row_off=0, width=src.width, height=src.height)
    red_window = nir_window
    green_window = nir_window
    blue_window = nir_window

    # Read the specific bands as numpy arrays
    nir_band = src.read(4, window=nir_window)
    red_band = src.read(3, window=red_window)
    green_band = src.read(2, window=green_window)
    blue_band = src.read(1, window=blue_window)
    
    # Perform the calculations
    trvi = 4 * ((nir_band - red_band) / (nir_band + red_band + green_band + blue_band))
    print(trvi)