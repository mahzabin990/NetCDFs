from osgeo import gdal
#This function, transform_netcdf, takes the netcdf_file as input. 
# It uses gdal.Open to open the NetCDF file in read-only mode and assigns the opened dataset to the variable dataset.
def transform_netcdf(netcdf_file):
    # Open the NetCDF file using gdal
    dataset = gdal.Open(netcdf_file, gdal.GA_ReadOnly)
#The GetSubDatasets method retrieves the subdatasets (also known as variables) from the NetCDF file.
#It returns a list of subdataset information, where each item in the list contains the name and description of a subdataset.
    # Get the subdatasets (variable names)
    subdatasets = dataset.GetSubDatasets()
#This loop iterates over each subdataset retrieved from the NetCDF file. Each subdataset is a tuple containing the subdataset name and description.
#The subdataset name is extracted and assigned to the variable subdataset_name.
    # Iterate over each subdataset (variable)
    for subdataset in subdatasets:
        # Get the subdataset name
        subdataset_name = subdataset[0]
#The variable name is extracted from the subdataset name.
# In NetCDF files accessed through gdal, the subdataset name includes the file name and the variable name separated by a colon (e.g., "netcdf_file:variable_name").
# The line uses split(":")[-1] to split the string at the colon and retrieve the last part, which represents the variable name. strip() is then used to remove any leading or trailing whitespace from the variable name.
        # Extract the variable name from the subdataset name
        var_name = subdataset_name.split(":")[-1].strip()
#This line creates the output filename for the GeoTIFF file. It uses an f-string to concatenate the var_name (the extracted variable name) with the ".tif" extension.
        # Create the output filename based on the variable name
        output_file = f'{var_name}.tif'
#gdal.Translate is used to convert the subdataset (variable) to GeoTIFF format. It takes the output filename (output_file), the subdataset name (subdataset_name), and the desired output format (format='GTiff'). 
# The function automatically detects the coordinate system and spatial extent of the subdataset and generates the corresponding GeoTIFF file.
        # Translate the subdataset to GeoTIFF
        gdal.Translate(output_file, subdataset_name, format='GTiff')

    # Close the dataset
    dataset = None
#This line closes the NetCDF dataset by assigning None to the dataset variable, releasing the resources associated with it.
# Example usage
netcdf_file = "cami_0000-09-01_64x128_L26_c030918.nc"
transform_netcdf(netcdf_file)

