CCPBioSim Documentation
=======================

<p align="center">
    <img src="docs/source/_static/logos/CCPBioSim-logo-white-bottom-text.svg#gh-dark-mode-only" alt="CCPBioSim logo" width="300"/>
    <img src="docs/source/_static/logos/CCPBioSim-logo-black-bottom-text.svg#gh-light-mode-only" alt="CCPBioSim logo" width="300"/>
</p>

One page that links to the documentation for every CCPBioSim project, hosted at [ccpbiosim.readthedocs.io](https://ccpbiosim.readthedocs.io/).

## Project Status

| Category       | Badges |
|----------------|--------|
| **Build**      | [![PR Checks](https://github.com/CCPBioSim/CCPBioSim/actions/workflows/pr.yaml/badge.svg)](https://github.com/CCPBioSim/CCPBioSim/actions/workflows/pr.yaml) |
| **Documentation** | [![Weekly Docs](https://github.com/CCPBioSim/CCPBioSim/actions/workflows/weekly-docs.yaml/badge.svg)](https://github.com/CCPBioSim/CCPBioSim/actions/workflows/weekly-docs.yaml) [![Docs - Status](https://app.readthedocs.org/projects/ccpbiosim/badge/?version=latest)](https://ccpbiosim.readthedocs.io/en/latest/) |

## Adding a project

Add a card for the project to `docs/source/index.rst`, under the section that fits it best.

## Building the docs

```bash
pip install -e ".[docs]"
make -C docs html
```

The pages are built into `docs/build/html`.
