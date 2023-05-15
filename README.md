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
- Instal dependencies
    ```bash
    pip install -r requirements.txt
    ```
- Create a ```.env``` file with these variables, as shown in .env_template:
    ```bash
    URL=https://www.trafikoa.euskadi.eus/servicios/IncidenciasTDT/IncidenciasTrafikoTDTGeo
    APRS_SERVER_URL=euro.aprs2.net
    APRS_SERVER_PORT=14580
    CALLSIGN=<YOUR_CALLSIGN>
    CALLSIGN_SSID=<DESIRED_SSID>
    CALLSIGN_PASS=<APRS.IS_PASSWORD>
    ```

## How to run the script
- With the virtual environment activated and a .env file created and filled, we are ready to run the script!

```bash
python main.py
```

## References and useful links

- https://aprs.fi
- https://davidpardavila.com/como-convertir-coordenadas-geograficas/
- https://www.omnicalculator.com/conversion/coordinates-converter#how-to-convert-coordinates-in-dd-to-dms-or-ddm
- https://github.com/EvanVS/APRS-Python