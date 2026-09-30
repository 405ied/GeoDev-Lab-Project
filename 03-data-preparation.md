# Data preparation

**Week 3 deliverable.** GeoDev Lab Africa, Cohort One.
Author: Akeem Lasisi

What I reprojected, what I clipped, what I checked, and what I fixed.

---

## 1. Coordinate system decisions

**Working CRS:** <EPSG:32631>

**Why this one:** i converted CRS to EPSG: 32631 Zone 31N because i would be making measurements in Meters or Kilo Meters which the EPSG: 4326 will give me wrong calculations

| Dataset | CRS as downloaded | CRS after | Operation |
|---|---|---|---|
| Administrative boundaries | EPSG:4326 | EPSG:32631 | Reprojected |
| Road Network | EPSG:4326 | EPSG:32631 | Reprojected |
| SRTM DEM |EPSG:32631 | EPSG:32631 | No change needed |

> Reprojecting recalculates every coordinate. Assigning a CRS only
> relabels the data. Say which one you did.

## 2. Clipping to the study area

- **Boundary used:** OSM and Roads Network
- **Features before clipping:** 15528
- **Features after clipping:** 9548

i clipped point feature of Places within the study Area some point fall just outside the Area and i kept them 

## 3. The five quality checks

| Check | Result | Action taken |
|---|---|---|
| Is the CRS what I think it is? | yes | Reprojected it |
| Are there nulls in the fields I need? | no | nothing |
| Are there duplicate features? | No | Nothing |
| Is the geometry valid? | <count invalid> | <what you did> |
| Does coverage span the whole study area? | no> | Clipped Ward Close to the Border |

## 4. Problems found, and what I did

**<Problem.>** <What it was, and whether you fixed it or flagged it.
Flagging honestly is acceptable. Hiding it is not.>

## 5. The analysis-ready output

- **File:** `data/processed/PST_Trunk_Roads.gpkg`
- **Format:** GeoPackage
- **CRS:** <EPSG:32631>
- **Features:** 191
- **Produced by:**  manually in QGIS

---

**Status:** Week 3 complete. First spatial analysis in Week 4.
