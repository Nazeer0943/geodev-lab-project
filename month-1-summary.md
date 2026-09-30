# 1.    Your question, restated in one sentence
What are the wards in Dutsi LGA that are not within 5Km zone of clinics
# 2. Which operation you ran and why that one
I ran a buffer a operation because it is the analysis that could allow me to drawa a kind of radius distance to the clinics
# 3. What you expected, and what you got
I expected to see some of the wards that the dissolved result of 5km buffer would not cover, and that would have told me the wards are outside the radius of 5km clinics. But I finally realized that there are no wards in Dutsi LGA that the residents can travel for 5km without seeing clinics
# 4.  What surprised you
I was suprised to see that the dissolved result of the buffer covered the entire wards layer
What surprised you  
# 5. What data you still need 'NA

Week 3 Quality Checks Performed:

CRS Verification: Checked that all layers were successfully reprojected from geographic coordinates (EPSG:4326) to projected meters (EPSG:32632 - UTM Zone 32N) to allow accurate area and distance measurements.

Geometry Check: Inspected polygon boundaries for self-intersections, gaps, or invalid geometries before running the buffer.

Attribute Integrity: Verified that the attribute tables for the wards and health facility points retained all required fields after clipping and exporting.


"Conclusion: Based on the 5 km buffer analysis around health facilities in Dutsi LGA, all wards fall within the 5 km service coverage zone, meaning there are no underserved wards according to this threshold."
