# Muhammed Enes Duran

Data scientist and ML engineer working on GeoAI, evaluation systems, spatial software, and remote-sensing pipelines.

[Portfolio](https://muend.github.io) · [PyPI](https://pypi.org/user/muend/) · [itch.io](https://muend.itch.io) · [Email](mailto:edcoders@gmail.com)

## Current work

| Project | Focus | Status |
|---|---|---|
| [benchfck](https://github.com/muend/benchfck) | Deterministic benchmark generation and exact scoring for controlled machine-state tasks | v0.4.0-alpha engineering candidate; no model results published |
| [geoai-skills](https://github.com/muend/geoai-skills) | Measured Agent Skills for geospatial AI | 18 skills with a published routing benchmark and known limitations |
| [arcgis-mcp-bridge](https://github.com/muend/arcgis-mcp-bridge) | Local-first ArcGIS Pro automation over MCP | Available on [PyPI](https://pypi.org/project/arcgis-mcp-bridge/) |
| [sentinel-crop-pipeline](https://github.com/muend/sentinel-crop-pipeline) | Reproducible Sentinel-2 preparation for crop-classification research | Open-source pipeline with spatially blocked dataset preparation |
| [agri-dss](https://github.com/muend/agri-dss) | Spatial decision support for agriculture | [Live application](https://tarimsalkoridor.online) |

## Selected projects

### benchfck

A Brainfuck-based generator and Rust harness for producing, validating, and scoring controlled machine-state tasks. Execution, cross-encoding equivalence, answer verification, and metrics are deterministic; the project does not use a learned judge. The current alpha is an engineering candidate, not a published model benchmark.

### geoai-skills

An Agent Skills-compatible suite covering geospatial data engineering, remote sensing, spatial statistics, GeoAI, databases, cartography, and controlled ArcGIS Pro execution. The project emphasizes CRS and unit checks, leakage-resistant validation, explicit uncertainty, reproducible evidence, and honest stop conditions.

### arcgis-mcp-bridge

A secure, local-first MCP server that exposes ArcGIS Pro's ArcPy engine over stdio JSON-RPC. It keeps the licensed GIS runtime isolated from the host process and validates paths before filesystem or geodatabase operations.

### sentinel-crop-pipeline

A configuration-driven pipeline for discovering, preprocessing, and patching Sentinel-2 L2A imagery into training-ready datasets. It includes cloud-aware filtering, ground-truth integration, spectral processing, and spatially blocked splits.

### Applied spatial systems

- [agri-dss](https://github.com/muend/agri-dss): agricultural suitability and decision-support software for the Western Antalya corridor.
- [kutri-resilience-index](https://github.com/muend/kutri-resilience-index): a reproducible five-pillar urban-territorial resilience index prototype.
- [turkiye-housing-prices-pandemic](https://github.com/muend/turkiye-housing-prices-pandemic): inflation-adjusted regional housing analysis with spatial statistics.
- [Studyo Rehberi](https://github.com/muend/studyo_rehberi): an accessible planning and zoning study guide for Kaş and Antalya.
- [FOUNDER.EXE](https://muend.itch.io/founderexe): a browser-based startup simulation built around financing, regulation, taxes, and runway decisions.

## Areas of focus

- Evaluation harnesses, reproducibility, and evidence boundaries
- GeoAI agent systems and spatial-method safeguards
- MCP infrastructure and local GIS automation
- Remote sensing, spatial ML, and leakage-resistant validation
- Decision-support and simulation products

## Technical work

Python, Rust, SQL, JavaScript, PyTorch, TensorFlow, scikit-learn, GeoPandas, Rasterio, PySAL, ArcPy, FastAPI, Pydantic, Docker, pytest, and GitHub Actions.

## Contact

For collaboration on GeoAI, evaluation infrastructure, spatial ML, or research software: [edcoders@gmail.com](mailto:edcoders@gmail.com).

