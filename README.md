# U.S States

U.S States is a python package that provides information about states. This package is currently being built, so there is some information that will be missing at the moment.

<a><img alt="GitHub contributors" src="https://img.shields.io/github/contributors/AColocho/us-states?color=%234B0082&style=plastic">
<img alt="GitHub issues" src="https://img.shields.io/github/issues/AColocho/us-states?style=plastic">
<img alt="GitHub closed issues" src="https://img.shields.io/github/issues-closed/AColocho/us-states?color=%23008000&style=plastic">
</a>

## Documentation:

### **Install**

The package can be downloaded from PyPi by using pip3 in the following way:

```
pip3 install unitedstates
```

### **States**

Before we get started, we need to define if we will grant DC statehood.

```python
# If DC will be counted as a state
from states import States_Abbreviated
states_abbreviated = States_Abbreviated(DC_Statehood=True)

# If DC will not be counted as a state
from states import States_Full_Name
states_full_name = States_Full_Name(DC_Statehood=False)
```

States are divided by regions and divisions in accordance with the U.S Census. The following are the divisions, which are class attributes.

- east_north_central
- east_south_central
- mid_atlantic
- mountain
- new_england
- pacific
- south_atlantic
- west_north_central
- west_south_central

```python
mountain_states = states_full_name.mountain
```

The following are regions, which are class attributes.

- northeast_region
- midwest_region
- south_region

In order to retrieve all the states, the `all_states` attribute can be used.

These attributes can be found on both `States_Full_Name()` and `States_Abbreviated()` classes.

This package contains information about each state. Here is a list of the information that is included:

- official_name
- full_name
- abbreviated
- capital
- population
- area_sq_km
- time_zone
- region

In order to retrieve this info, the `get_states_info()` method can be used.

```python
from states import States
states = States()
virginia_info = states.get_state_info('Virginia')
```

Which would return the following:

```
{   "official_name":"Commonwealth of Virginia",
    "full_name":"Virginia",
    "abbreviated":"VA",
    "capital":"Richmond",
    "population": 8535519,
    "area_sq_km":110786,
    "time_zone": ["Eastern Standard Time","GMT-5"],
    "region":"South Atlantic"}
```

**Keep in mind** that some states contain more than one time zone depending on which town you are located in. At the moment, the info only contains the major ones.

You can pull all the available states by passing the function "all".

### **Territories**

You can access the territory classes by importing them from states.
Territories have the following classes:

- Territories_Abbreviated
- Territories_Full_Name
- Associated_States
- Uninhabitated_Territories

```python
from states import Territories_Abbreviated
```

Both the `Territories_Abbreviated` and `Territories_Full_Name` contain the following attributes:

- atlantic
- pacific
- all_territories

```python
atlantic_territories = Territories_Abbreviated().atlantic
```

`Associated_States` contains the following attributes:

- pacific_abbreviated
- pacific_full_name

`Uninhabitated_Territories` contains the following attributes:

- all_territories

This package contains information about each state, here is a list of the info included:

- official_name
- full_name
- abbreviated
- capital
- population
- area_sq_km
- time_zone
- region

In order to retrieve this info, the `get_territory_info()` method can be used.

```python
from states import Territories
territories = Territories()
virginia_info = territories.get_territory_info('Puerto Rico')
```

Which would return the following:

```
{   "official_name":"Commonwealth of Puerto Rico",
    "full_name":"Puerto Rico",
    "abbreviated":"PR",
    "capital":"San Juan",
    "population": 3193694,
    "area_sq_km":9104,
    "time_zone": ["Atlantic Standard Time","GMT-4"],
    "region":"Atlantic"}
```

You can pull all the available territories by passing the function "all".

## Contribution:

We welcome anyone who wants to contribute. Please see the contribution page for guidelines on contributing and submitting feature requests.

## Resources used:

- https://www2.census.gov/geo/pdfs/maps-data/maps/reference/us_regdiv.pdf
- https://www.corporateservices.noaa.gov/finance/docs/AOD/LIST_OF_US_TERRITORIES.pdf
- https://www.cdc.gov/publichealthgateway/oia/territories-states.html
- https://www.txdmv.gov/sites/default/files/body-files/State_and_Country_Codes.pdf
- https://www.cia.gov/the-world-factbook/
- https://www.census.gov/schools/facts/
