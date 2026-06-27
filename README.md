<p align="center">
  <img src="./assets/banner.svg" alt="Muhammed Enes Duran — Data Scientist & ML Engineer · Spatial Data Science · GeoAI · Deep Learning for Remote Sensing">
</p>

<p align="center">
  <a href="https://tarimsalkoridor.online"><img src="https://img.shields.io/badge/Live_App-tarimsalkoridor.online-0A7D32?style=flat-square&logo=vercel&logoColor=white"></a>
  <a href="mailto:edcoders@gmail.com"><img src="https://img.shields.io/badge/Email-edcoders@gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white"></a>
</p>

I build production-grade GeoAI: spatial decision-support systems, ArcGIS automation exposed to LLM agents, and deep-learning pipelines for satellite imagery — connecting rigorous mathematical models to systems people can actually use.

<p align="center">
  <img src="https://img.shields.io/badge/MCP_geoprocessing_tools-100-13140F?style=for-the-badge">
  <img src="https://img.shields.io/badge/neighborhoods_modeled-147-13140F?style=for-the-badge">
  <img src="https://img.shields.io/badge/SaaS-live_in_production-0A7D32?style=for-the-badge">
  <img src="https://img.shields.io/badge/TÜBİTAK_2209--A-grant_funded-0A7D32?style=for-the-badge">
</p>

---

## Technical Core & Methodology

I focus on structural data science and deep learning architectures, building robust end-to-end machine learning pipelines (*O(N)* efficiency), data ingestion engines, and secure automation interfaces that connect mathematical models with complex enterprise systems.

**Core AI/ML**
<br>
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white)

**Spatial Data Science**
<br>
![GeoPandas](https://img.shields.io/badge/GeoPandas-139C5A?style=flat-square)
![Shapely](https://img.shields.io/badge/Shapely-4B8BBE?style=flat-square)
![ArcPy](https://img.shields.io/badge/ArcPy_(ArcGIS_Pro)-2C7FB8?style=flat-square&logo=arcgis&logoColor=white)
![Rasterio](https://img.shields.io/badge/Rasterio-3776AB?style=flat-square)
![PySAL](https://img.shields.io/badge/PySAL-EE4C2C?style=flat-square)

**MLOps & Infrastructure**
<br>
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic_v2-E92063?style=flat-square&logo=pydantic&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC?style=flat-square&logo=pytest&logoColor=white)
![Ruff](https://img.shields.io/badge/Ruff-D7FF64?style=flat-square&logo=ruff&logoColor=black)
![Mypy](https://img.shields.io/badge/Mypy-2A6DB2?style=flat-square)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

---

## Flagship Systems & ML Infrastructure

### 1. [arcgis-mcp-bridge](https://github.com/muend/arcgis-mcp-bridge)

An institutional-grade Model Context Protocol (MCP) framework exposing exactly **100 specialized geoprocessing tools** directly to LLM hosts and intelligent agents — turning ArcGIS Pro into a programmable backend for AI workflows.

- **Process Isolation:** Built with a strict decoupled multi-process architecture (Async Core / Isolated Worker Subprocess) to guarantee runtime protection against environment blockages.
- **Security Layer:** Features a strict PathGuard sandbox enforcing prefix validation over database structures before any algorithmic execution occurs.

```mermaid
flowchart LR
    A["LLM Host / AI Agent"] -->|MCP protocol| B["MCP Server<br/>Async Core"]
    B --> C{"PathGuard<br/>sandbox"}
    C -->|path validated| D["Isolated Worker<br/>Subprocess"]
    C -.->|rejected| X["Blocked"]
    D --> E["ArcGIS Pro · ArcPy"]
    E --> F["100 geoprocessing tools"]
```

### 2. [agri-dss](https://github.com/muend/agri-dss) &nbsp;—&nbsp; Live at [tarimsalkoridor.online](https://tarimsalkoridor.online)

A fully client-side Spatial Decision Support System (Agri-DSS) for the Western Antalya agricultural corridor — **5 districts, 147 neighborhoods** (Demre, Finike, Kaş, Kemer, Kumluca) — turning local agronomic and economic knowledge into a concrete, printable plan for each neighborhood: seasonal crops rated by yield and profitability, a long-term orchard investment, and an emerging market opportunity.

- **Zero-Backend Static Architecture:** A single vanilla-JS `index.html` carrying all DSS logic against a decoupled `data.json` layer — no backend, no build step. Trivially hostable on GitHub Pages, instantly auditable, and immune to server outages.
- **DRY Data Contract:** A compact `cropSets` / `longTermCrops` / `regions` structure resolved at runtime — recommendations can be updated by editing `data.json` alone, with no code changes.
- **Swiss / Typographic Interface:** International Typographic Style UI (Archivo + Space Mono, modular grid, single agricultural-green accent) with a guided stepper, corridor diagram, and live counters — collapsing to a clean ink-on-white **A4 print layout** for village boards and cooperatives.

<p align="center">
  <a href="https://tarimsalkoridor.online"><img src="./assets/agri-dss-preview.png" alt="Agri-DSS live application interface" width="82%"></a>
</p>

---

## Academic & Research Projects

Reproducible, peer-review–oriented studies in spatial econometrics, urban resilience, and deep learning for remote sensing.

### [agri-unet](https://github.com/muend/agri-unet) &nbsp;·&nbsp; `Deep Learning / CV` &nbsp;·&nbsp; ![TÜBİTAK 2209-A](https://img.shields.io/badge/TÜBİTAK_2209--A-Funded-0A7D32?style=flat-square)

The codebase for my **TÜBİTAK 2209-A** research project (*University Students Research Projects Support Program*) — an accepted, grant-funded study. A **U-Net** semantic segmentation pipeline for agricultural pattern identification from high-resolution, multi-temporal satellite imagery, extracting field parcels and crop structures for downstream suitability modeling.

### [turkiye-housing-prices-pandemic](https://github.com/muend/turkiye-housing-prices-pandemic) &nbsp;·&nbsp; `Spatial Econometrics`

Region-level analysis of Türkiye's housing market that separates real (inflation-adjusted) price growth from inflation, comparing the six years before and after the COVID-19 pandemic (2014–2025).

- Reproducible Python notebook with high-resolution choropleth figures and a House Price Index (HPI) deflation pipeline.
- **LISA** (Local Indicators of Spatial Association) analysis to detect statistically significant regional clusters and spatial outliers.

### [kutri-resilience-index](https://github.com/muend/kutri-resilience-index) &nbsp;·&nbsp; `Composite Indicators`

A reproducible urban-territorial resilience index prototype for Kaş / Bayındır, Antalya, based on a five-pillar composite indicator framework.

- Transparent indicator normalization and weighting methodology with fully reproducible notebooks and figures.
- Bridges quantitative spatial analysis with applied territorial planning.

---

## Featured Repositories

<p>
  <a href="https://github.com/muend/arcgis-mcp-bridge"><img src="https://github-readme-stats.vercel.app/api/pin/?username=muend&repo=arcgis-mcp-bridge&theme=graywhite&hide_border=true&v=2"></a>
  <a href="https://github.com/muend/agri-dss"><img src="https://github-readme-stats.vercel.app/api/pin/?username=muend&repo=agri-dss&theme=graywhite&hide_border=true&v=2"></a>
</p>

---

## Active Research & Deep Learning Workspace

- **Computer Vision for Remote Sensing:** Formulating automated pipelines for agricultural pattern identification and urban object extraction from high-resolution multi-temporal satellite imagery using Convolutional Neural Networks (CNN) and U-Net segmentation models.
- **Urban Resilience Forecasting:** Engineering predictive spatial suitability matrices and long-term geometric resilience frameworks for horizon target lines using robust statistical models.

---

## Focus

Open to collaborative tracks involving production-grade Data Science, Spatial Machine Learning pipelines, and automated GeoAI systems architecture.

- **Live App:** [tarimsalkoridor.online](https://tarimsalkoridor.online)
- **Email:** [edcoders@gmail.com](mailto:edcoders@gmail.com)
