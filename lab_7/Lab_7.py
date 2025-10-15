import arcpy

# Assign bands
source = r"E:\GEOG676\Lab7_Data"
band1 = arcpy.sa.Raster(source + r"\band01.tif") # Blue
band2 = arcpy.sa.Raster(source + r"\band02.tif") # Green
band3 = arcpy.sa.Raster(source + r"\band03.tif") # Red
band4 = arcpy.sa.Raster(source + r"\band04.tif") # NIR
combined = arcpy.CompositeBands_management([band1, band2, band3, band4], source + r"\output_combined.tif")

# Hillshade
azimuth = 315
altitude = 45
shadows = 'NO_SHADOWS'
z_factor = 1
arcpy.ddd.HillShade(source + r"\dem.tif", source + r"\output_Hillshade.tif", azimuth, altitude, shadows, z_factor)

# Slope
output_measurement = "DEGREE"
z_factor = 1
arcpy.ddd.Slope(source + r"\dem.tif", source + r"\output_Slope.tif", output_measurement, z_factor)

print("success!")