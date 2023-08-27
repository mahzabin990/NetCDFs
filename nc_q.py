import netCDF4

# Path to the NetCDF file
netcdf_path = 'cami_0000-09-01_64x128_L26_c030918.nc'

# Open the NetCDF file using netCDF4
dataset = netCDF4.Dataset(netcdf_path)

# Get variable count and names
variable_count = len(dataset.variables)
variable_names = list(dataset.variables.keys())

# Print the variable count and names
print(f"Q: How many variables are there in the NetCDF file?")
print(f"A: There are {variable_count} variables.")
print(f"Q: What are the variable names?")
print(f"A: The variable names are: {', '.join(variable_names)}")

# Get variable information
for var_name in variable_names:
    variable = dataset.variables[var_name]
    var_attributes = variable.ncattrs()
    print(f"Q: What are the attributes of the variable '{var_name}'?")
    for attr in var_attributes:
        attr_value = variable.getncattr(attr)
        print(f"A: The attribute '{attr}' of the variable '{var_name}' is '{attr_value}'.")

# Close the dataset
dataset.close()


