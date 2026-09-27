# Data notes



## GRID3 Nigeria Operational LGAs v3.0

- Source: https://data.grid3.org

Downloaded: 9/27/2026

- 774 features, polygons

- Columns: FID(Integer (64 bit)), globalid(Text (string)), unique_id(Integer (32 bit)), timestamp(Date & Time), editor(Text (string)), Iganame(Text (string)), Igacode(Text (string)), statename(Text (string)), statecode(Text (string)), source(Text (string)), amapcode(Text (string)).

- No nulls in lga\_name

- Covers my LGA fully



## GRID3 Nigeria Operational Wards v3.0

- Source: https://data.grid3.org

Downloaded: 9/27/2026

- 5872 features, polygons

- Columns: OBJECTID(Int 64), country(string), iso3(string), state(string), statecode(string),lga(string),Iga_alt_names(string), ward(string), ward_alt_names(string), ward_v1_grid3(string), ward_in_grid3_ward_list(Real),
multipart_count(Real), source(string), date(string), area_sqkm(Real).

- No nulls in ward column

- Covers my LGA fully


## OSM higways, extracted via QuickOSM

- Query: highways in Katsina(Dutsi LGA)

- Extracted: 9/27/2026

- 175  features (lines)
- Field

- Fields; fid(int 64), full id(string), , osm_id(string), osm_type(string), highway(string), ford(string), oneway(string), junction(string), layer(string),bridge(string), surface(string), ref(string).

- I did not see null values across all the fields.


- Coverage looks good 

## CRS and preparation
- All source layers arrived in EPSG:4326
- Study area: Dutsi, extracted from GRID3 LGAs and Wards
### All layers clipped to study area, then reprojected to EPSG:32632 (UTM 32N)
- Area check: Dutsi LGA 370 km2, matches published figure
- Working files in data/processed/, raw files untouched



## CRS and preparation
- All source layers arrived in EPSG:4326
- Study area: Dutsi, extracted from GRID3 LGAs
### All layers clipped to study area, then reprojected to EPSG:32632 (UTM 32N)
- Area check: Dutsi LGA 370 km2, matches published figure
- Working files in data/processed/, raw files untouched
