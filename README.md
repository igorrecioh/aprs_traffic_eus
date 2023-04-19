# aprs_traffic_eus

## Data source

Traffic incidents are gathered from the official [Open Data website](https://opendata.euskadi.eus/catalogo/-/incidencias-trafico-euskadi/) of the Basque Government 

## Environment set up
- Create virtual environment:
    ```bash
    python3 -m venv myvenv
    ```
- Activate virtual environment
    ```bash
    source myvenv/bin/activate
    ```
- Create a ```.env``` like with these variables:
    ```bash
    URL=https://www.trafikoa.euskadi.eus/servicios/IncidenciasTDT/IncidenciasTrafikoTDTGeo
    ```

## How to run the script
WIP