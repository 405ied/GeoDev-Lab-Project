# Project brief

**Week 1 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Akeem Lasisi

---

## 1. The question

> The aim is to assess relative border-outpost suitability and terrain accessibility along the Nigeria–Benin border in Ogun State using publicly available geospatial data, remote sensing and GIS-based multi-criteria analysis.

## 2. Why this question

1. To acquire, prepare and assess the quality of public environmental and infrastructural datasets for the study area.

2. To characterise land cover and terrain conditions using satellite imagery and elevation data.
3. To develop a transparent multi-criteria model of relative border-outpost suitability.
4. To assess broad spatial patterns of terrain accessibility and their relationship with modelled suitability.
5. To evaluate sensitivity to criterion weights, standardisation assumptions and analytical resolution.


## 3. Study area

The study focuses on western Ogun State and the selected LGAs shown in the researcher's map. The final spatial description will be derived from checked boundary data and verified published sources. It will report the actual area, coordinate extent, land-cover composition and terrain distribution after these quantities have been calculated.
Boundary naming, geometry and dataset provenance will be reconciled before analysis. The location map will distinguish the selected reporting area from the international boundary and show Nigeria, Ogun State and the selected LGAs at appropriate scales. Every map frame will have its own verified scale information. The final layout will state the full coordinate reference system and source versions.

## 4. What I mean by the terms

- Suitability is the relative compatibility of a location with the criteria and assumptions used in the assessment. It is not a probability of successful operation.

- Terrain accessibility denotes a relative description of physical movement conditions and mapped infrastructural access. It does not denote measured journey time, legal access or a recommended route.

- A factor is an attribute that influences relative preference; a constraint is an explicitly justified condition that excludes an area from assessment. Missing data are neither a factor score nor an exclusion criterion.

- Sensitivity analysis examines how outcomes change when assumptions or inputs vary. 

- Desktop assessment denotes research conducted with existing data and computer-based analysis without field data collection.


## 5. Datasets

No link, no dataset. Every row below has a source you have opened yourself.

| # | Dataset | What it gives me | Source |
|---|---|---|---|
| 1 | Administrative boundaries | Study extent and reporting units; verify names, geometry, release and adjacency | https://data.grid3.org/datasets/GRID3::grid3-nga-operational-lga-boundaries/about |
| 2 | Optical imagery | Land-cover interpretation; record bands, dates, cloud masks and product metadata | https://download.dataspace.copernicus.eu/odata/v1/Products(99e3e71a-3eb2-4c2b-ae49-dbfb43b75290)/$value|
| 3 | Elevation | Terrain characterisation; inspect voids, units, surface effects and acquisition age | https://doi.org/10.5069/G9445JDF |
| 4 | Roads and settlements | Public infrastructure context; check duplicates, completeness and date | https://portal.opentopography.org/datasetMetadata?otCollectionID=OT.042013.4326.1 |
| 5 | Land-cover comparison | Contextual comparison; reconcile class definitions and observation periods | https://sentiwiki.copernicus.eu/web/s2-processing |
| 6 | <name> | <what it contributes> | <https://...> |

GRID3 (n.d.) lists Nigerian spatial products, while Geofabrik (n.d.) provides downloadable OpenStreetMap extracts. The exact releases will be entered in a data register after acquisition. SRTMGL1 V003 is an approximately 30 m elevation product derived principally from the February 2000 mission (NASA JPL, 2013). These dates will not be represented as contemporary observations of all surface conditions.

## 6. What "done" looks like

The expected outputs are a documented spatial database, a land-cover assessment, terrain and accessibility summaries, relative suitability maps, sensitivity maps, and a reproducible QGIS project with a processing log. The final thesis will discuss where the evidence supports interpretation and where additional investigation would be needed.

## 7. Known risks

**<Risk one.>** <What could go wrong and what you will do about it.>

**<Risk two.>** <Same.>

---

**Status:** Week 1 complete. Data acquisition in Week 2, see
[02-data-notes.md](02-data-notes.md).
