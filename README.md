# Snelnotuleren Python SDK

[![PyPI version](https://badge.fury.io/py/snelnotuleren-sdk.svg)](https://badge.fury.io/py/snelnotuleren-sdk)
[![Python versions](https://img.shields.io/pypi/pyversions/snelnotuleren-sdk.svg)](https://pypi.org/project/snelnotuleren-sdk/)

De officiële Python SDK voor de Snelnotuleren API.

## Installatie

```bash
pip install snelnotuleren
```

## Quick Start

```python
from snelnotuleren import SnelNotulerenClient

# Initialiseer de client
client = SnelNotulerenClient(
    client_id='your_client_id',
    client_secret='your_client_secret'
)

# Maak een order aan
order_id = client.create_order(
    file_path='vergadering.mp3',
    email='contact@bedrijf.nl',
    context='Maandelijkse vergadering',
    report_type='transcriptie'  # Of: korte_notulen, middel_notulen, lange_notulen
)
```

## Rapport Types & Prijzen

| Type | Prijs | Beschrijving |
|------|-------|--------------|
| transcriptie | €5 | Volledige transcriptie |
| korte_notulen | €10 | Beknopte samenvatting |
| middel_notulen | €20 | Gebalanceerde notulen |
| lange_notulen | €25 | Uitgebreide notulen |

## Uitgebreide Voorbeelden

### Met alle opties
```python
order_id = client.create_order(
    file_path='vergadering.mp3',
    email='contact@bedrijf.nl',
    context='Bestuursvergadering Q1',
    report_type='middel_notulen',
    smart_detection=True,     # Automatische agendapunt detectie
    speaker_diarization=True, # Sprekerherkenning
    speaker_count=4          # Aantal verwachte sprekers
)
```

## Development

```bash
# Installeer dependencies
pip install -r requirements.txt
```

## Links

- [API Documentatie](https://api.snelnotuleren.nl/docs)
- [Support](niels@snelnotuleren.nl)

## License

[MIT License](LICENSE)