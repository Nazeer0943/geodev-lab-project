# **Nazir Sani, Pod 12**

# Geodev Lab Africa - Month 1 Project

**Core Research Question:** Which wards in Dutsi LGA, Katsina State, are more than 5 km from a health facility?

**Final Answer / Result:** After performing a 5 km dissolved buffer analysis around all health facilities in Dutsi LGA using projected coordinates (EPSG:32632), the analysis reveals that **all wards fall completely within the 5 km service coverage zone**, meaning there are no underserved wards based on this distance threshold.

Built with GeoDev Lab Africa, Cohort One. This repository compiles a complete four-week geospatial analysis workflow examining healthcare accessibility in Dutsi LGA.

---

## 📁 Project Structure & Weekly Work

* **Week 1: Project Brief**
  * [`project-brief.md`](./project-brief.md) — Outlines the core research question and exact data source links.

* **Week 2: Data Notes**
  * [`data-notes.md`](./data-notes.md) — Documents the datasets downloaded, initial CRS inspections, and data structures.

* **Week 3: Data Preparation & Quality Checks**
  * [`data/processed/`](./data/processed/) — Contains the prepared, reprojected spatial data layers (UTM Zone 32N / EPSG:32632) and quality check documentation.

* **Week 4: Analysis & Final Summary**
  * [`month-1-summary.md`](./month-1-summary.md) — Final findings and spatial analysis write-up.
  * [`5KM_Clinics_buffer_Dutsi.png`](./5KM_Clinics_buffer_Dutsi.png) — Final map image showing the 5 km buffer analysis around health facilities.



## Month 2: development environment and early Python

- Week 5: set up Python, VS Code and the terminal. [`hello.py`](./hello.py) runs.

- Week 6: set up the project with `uv` and added pandas. [`check.py`](./check.py) prints the pandas version.

- Week 7: [`analyse.py`](./analyse.py) reads [`wards.csv`](./wards.csv), converts each area and classifies each ward.

- Week 8: I have added a few more rows to my [`wards.csv`](./wards.csv) file coupled with another field in number (`Pop`) to enable me conduct the summarization. One value from the `Pop` column was intentionally removed so that the concept of break could be tested. [`inspect_data.py`](./inspect_data.py) was used to inspect the data structure.

- Week 9: [`summary.py`](./summary.py) runs the capstone functions on my merged Katsina spatial dataset ([`Katsina_LGAs_and_Pop.csv`](./Katsina_LGAs_and_Pop.csv)).

---

### Month 2 Reflection

This month, the concept of writing reusable functions and handling tabular data structures finally clicked for me. Because of an instruction I saw lately on making sure the  functions works on actual data not on the wards.csv,  I had to use a "select features by expression in QGIS" extracted  LGAs in Katsina from the LGAs boundry and merge them with a population data via an attribute join, which I did beautifully, it did not work at the first place because the LGA code from the population data was a string not a number, but after using a field calculator and creating another LGA Code field as int, if tinally worked. 

