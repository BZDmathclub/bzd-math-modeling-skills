# CUMCM 2023 B - Multibeam Survey-Line Planning

## Metadata

- Sources: B题赛题 PDF and specialist post-contest analysis `多波束测线问题的问题解析`
- Authority: official problem plus expert analytical review; no official point table
- Ingested: 2026-08-13

## Task map and evidence anchors

| ID | Task | Observable full-credit evidence |
|---|---|---|
| B23-11 | Q1 slope coverage | Derives left/right swath widths on a sloped cross-section and total coverage with correct units/signs |
| B23-12 | Q1 overlap | Symmetric adjacent-swath overlap definition using both neighboring side widths; reduces to flat-bottom formula |
| B23-13 | Q1 outputs | Correct depths, widths and overlap sequence in the specified table |
| B23-21 | Q2 3D orientation | Derives projected along-line/cross-line slopes from beta and computes position-dependent depth/coverage |
| B23-22 | Q2 grid outputs | Complete 8-by-8 directional/distance coverage table and result file with symmetry/sign checks |
| B23-31 | Q3 direction proof | Justifies line direction (parallel to depth contours / perpendicular to horizontal slope projection) for shortest full coverage |
| B23-32 | Q3 recursive layout | Boundary-aware first/last lines and recursive spacing satisfying 10-20% overlap across the slope |
| B23-33 | Q3 optimality/result | Concrete coordinates, full-coverage proof, overlap audit and total length; reference construction uses 34 lines/68 nmi |
| B23-41 | Q4 terrain model | Reconstructs/interpolates bathymetry and partitions or otherwise represents locally varying slopes with error control |
| B23-42 | Q4 route design | Lines follow local contours where justified; design balances coverage, <=20% overlap and length |
| B23-43 | Q4 final audit | Calculates total length, missed-area percentage and length with overlap above 20% using actual depths, not fitted planes alone |

## Negative anchors and validation

- A one-sided overlap definition that changes when sailing direction reverses is invalid.
- Stating that north-south or another direction is optimal without derivation or comparison earns limited credit.
- Giving only the number/total length of lines without coordinates and construction is incomplete.
- For arbitrary terrain, designing on fitted planes but never recomputing actual-depth overlap/missed area is not validated.
- Subregions should have approximately parallel contours; otherwise refine them or quantify approximation error.
- Curved/nonparallel lines require a new defensible overlap definition and solution method, not merely a plotted route.

## Transferable lessons

- Geometric coverage criteria should satisfy invariance/symmetry sanity checks before numerical use.
- Planning on an approximation requires final evaluation on the original field/data.
- Score boundary coverage, interior recurrence, line coordinates and global metrics independently.
- Multi-objective route design should report all requested metrics rather than collapsing them into an unexplained weighted sum.

## Limits

The article supplies methods, reference results and common errors but no official point allocation or score distribution.
