# Month One Summary

## 1. The question

> Assess relative border-outpost suitability and terrain accessibility along the Nigeria–Benin border in Ogun State using publicly available geospatial data, remote sensing and GIS-based multi-criteria analysis.

## 2. Why this question

1. To acquire, prepare and assess the quality of public environmental and infrastructural datasets for the study area.

2. To characterise land cover and terrain conditions using satellite imagery and elevation data.
3. To develop a transparent multi-criteria model of relative border-outpost suitability.
4. To assess broad spatial patterns of terrain accessibility and their relationship with modelled suitability.
5. To evaluate sensitivity to criterion weights, standardisation assumptions and analytical resolution.

## 3. Datasets

No link, no dataset. Every row below has a source you have opened yourself.

| # | Dataset | What it gives me | Source |
|---|---|---|---|
| 1 | Administrative boundaries | Study extent and reporting units; verify names, geometry, release and adjacency | https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about |
| 2 | Optical imagery | Land-cover interpretation; record bands, dates, cloud masks and product metadata | https://download.dataspace.copernicus.eu/odata/v1/Products(99e3e71a-3eb2-4c2b-ae49-dbfb43b75290)/$value|
| 3 | Elevation | Terrain characterisation; inspect voids, units, surface effects and acquisition age | https://doi.org/10.5069/G9445JDF |
| 4 | Roads and settlements | Public infrastructure context; check duplicates, completeness and date | https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.042013.4326.1 |
| 5 | Land-cover comparison | Contextual comparison; reconcile class definitions and observation periods | https://sentiwiki.copernicus.eu/web/s2-processing |

## 4. Coordinate system decisions

**Working CRS:** <EPSG:32631>

**Why this one:** i converted CRS to EPSG: 32631 Zone 31N because i would be making measurements in Meters or Kilo Meters which the EPSG: 4326 will give me wrong calculations

| Dataset | CRS as downloaded | CRS after | Operation |
|---|---|---|---|
| Administrative boundaries | EPSG:4326 | EPSG:32631 | Reprojected |
| Road Network | EPSG:4326 | EPSG:32631 | Reprojected |
| SRTM DEM |EPSG:32631 | EPSG:32631 | No change needed |

# week 4

- Road selection by values
    Primary Roads
    Secondary Roads
    Tertiary Roads
    Trunk Roads

- Merged all selected Roads

- 1km Buffer was carried out on the Merged Roads
    Settlements and Places within 1km of the roads where intersected
- 52,229 Buildings/Physical Structures are within the Buffer
- They are 295 places/Villages within the Buffer Zone

- [x] Week 1, project brief with a source link for every dataset [the project brief](docs/01-project-brief.md)
- [x] Week 2, data downloaded, opened and described [Data Note](docs/02-data-notes.md)
- [x] Week 3, reprojected, clipped and quality checked
- [x] Week 4, first spatial analysis, checked four ways [Spatial Analysis](docs/04-Spatial-Analysis.md) and [First Month Summary](docs/05-Month-1-Summary.md)