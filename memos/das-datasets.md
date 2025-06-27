# A Guide to Open Distributed Acoustic Sensing (DAS) Datasets

Distributed Acoustic Sensing (DAS) is a technology that transforms a standard fiber optic cable into a dense array of thousands of individual vibration sensors.

Imagine a long glass fiber. A special device called an interrogator sends pulses of laser light down this fiber. As the light travels, tiny natural imperfections in the glass scatter a small amount of light back towards the interrogator. When the fiber is perfectly still, this pattern of backscattered light is stable.

However, if the fiber is stretched or compressed at any point—even by a microscopic amount—it changes the timing and phase of the light that is scattered back from that point. The interrogator measures these changes with extreme precision.

### What is the Connection to Pressure Sensing?

DAS measures **strain**, not pressure. It can only detect if the fiber itself is being stretched or squeezed.

Pressure waves cause strain. A pressure wave, like a seismic wave from an earthquake or a sound wave from a whale traveling through the ground or water, causes the surrounding material (rock, soil, water) to compress and expand.

The strain is transferred to the cable. If the fiber optic cable is well-coupled to its environment (e.g., buried in the seafloor), the compression and expansion of the surrounding material will squeeze and stretch the cable along with it.

Therefore, DAS senses a pressure wave by measuring its effect—the strain it induces on the fiber optic cable. Scientists can then analyze this strain data to infer the properties of the original pressure wave, effectively using the entire fiber optic cable as a long, continuous line of pressure sensors.

## Underwater DAS Datasets

This document provides a curated list of publicly available Distributed Acoustic Sensing (DAS) datasets from various projects around the world. These datasets are invaluable resources for research in seismology, oceanography, urban monitoring, geohazards, and more.

| Name                                                 | Summary                                                                                                                                              | Access Link                                                                                                                                 |
| :--------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| **OOI Regional Cabled Array (Oregon, USA, 2021)**    | A landmark subsea dataset rich with signals from earthquakes, whale vocalizations, and ship traffic. A key resource for marine seismology and bioacoustics. | [Link](http://piweb.ooirsn.uw.edu/das/)                                                                                                      |
| **Offshore Valencia Islalink (Spain, 2020)**         | A subsea (and landline) dataset for studying microseisms, ship noise, and marine life in the Mediterranean.           | [Globus Link](https://app.globus.org/file-manager?origin_id=706e304c-5def-11ec-9b5c-f9dfb1abb183&origin_path=%2FValencia%2F)                             |
| **DAS4Microseism (Svalbard, Norway, 2020)**          | A 42-day dataset focused on recording microseismicity in the Arctic, providing valuable data for cryoseismology and polar research.                     | [DOI: 10.18710/VPRD2H](https://doi.org/10.18710/VPRD2H) • [Mirror](https://dataverse.no/dataset.xhtml?persistentId=doi:10.18710/VPRD2H)     |
| **DAS4Whale (Svalbard, Norway, 2020)**               | A 2-day dataset specifically capturing baleen whale vocalizations in the Arctic, useful for marine bioacoustics and passive acoustic monitoring.          | [DOI: 10.5281/zenodo.5823343](https://doi.org/10.5281/zenodo.5823343)                                                                       |
| **Global DAS Month (Worldwide, February 2023)**       | Participating systems represent a variety of manufacturers, a range of recording parameters, and varying cable emplacement settings (e.g., shallow burial, borehole, subaqueous, and dark fiber). |  [Globus Link](https://app.globus.org/file-manager?origin_id=706e304c-5def-11ec-9b5c-f9dfb1abb183&origin_path=%2FDAS-Month-02.2023%2F) |


# Subaqueous and Near-Aquatic DAS Deployments (Global DAS Month – Feb 2023)

Here is a deeper look at Global DAS Month data:

| **Site / Project**        | **Location**               | **Environment**          | **Cable Type**           | **Potential Applications**                                           |
|--------------------------|----------------------------|--------------------------|---------------------------|----------------------------------------------------------------------|
| **ETH Zurich – Istanbul**| Istanbul, Turkey           | Sea shore                | Nearshore DAS             | Local seismicity, port activity, bioacoustics                       |
| **ETH Zurich – Limmat**  | Zurich, Switzerland        | River bank               | Urban/riverbank fiber     | Urban hydrodynamics, flood risk, infrastructure monitoring          |
| **IMS – Gran Canaria**   | Canary Islands, Spain      | Coastal, marine          | Subaqueous                | Whale vocalizations, surf zone processes, vessel noise              |
| **JAMSTEC – Muroto**     | Muroto, Japan              | Deep-sea cable           | Ocean-bottom cable        | Seafloor instability, submarine landslides, acoustic tomography     |
| **NTNU**                 | Svalbard, Norway          | Fjord/marine             | Coastal submerged cable   | Fjord circulation, ice-related noise, ecological interactions       |
| **Sandia – Alaska**      | Alaska, USA                | Coastal subarctic        | Subsea/permafrost edge    | Sea ice–ocean interaction, seasonal freeze-thaw monitoring          |
| **SusTech – XFJ**        | Shenzhen, China            | Estuary or shallow bay   | Coastal telecom fiber     | Estuarine dynamics, sediment plumes, anthropogenic noise detection  |
| **Tampnet**              | North Sea (offshore oil)   | Open sea                 | Submarine telecom cable   | Whale migration, shipping activity, offshore infrastructure health  |

---

## Classification by Application Domains

### 🌊 Oceanographic Monitoring
- JAMSTEC – internal waves, plume dynamics
- NTNU – fjord circulation, salinity layers
- SusTech – estuarine hydrodynamics

### 🐋 Bioacoustics & Marine Life
- IMS Gran Canaria – cetaceans, fish schools
- Tampnet – whale migration corridors
- ETH Istanbul – shallow bioacoustic monitoring

### ❄️ Ice & Climate
- Sandia – sea ice edge detection
- NTNU – sub-Arctic fjord ice conditions

### 🚢 Anthropogenic Impact & Hazards
- Tampnet – shipping noise, oil infrastructure risk
- ETH Limmat – urban infrastructure sensing
- JAMSTEC – submarine seismic events and cable stress

---


## Non-underwater DAS Datasets 

While there is a limited amount of open data for underwater DAS datasets, some of the following may contain both underwater and landline cables.

| Name                                                 | Summary                                                                                                                                              | Access Link                                                                                                                                 |
| :--------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| **Utah FORGE Project (Utah, USA, 2019, 2022+)**      | Extensive data from deep boreholes monitoring microseismicity during hydraulic stimulation for geothermal energy research. Multiple datasets are available. | [Link](https://gdr.openei.org/search?q=distributed%20acoustic%20sensing)                                                                    |
| **PoroTomo Project (Nevada, USA, 2016)**             | Data from horizontal and vertical DAS arrays at a geothermal field, including recordings of controlled explosions and natural seismic events.            | [Link](https://gdr.openei.org/submissions/980)                                                                                              |
| **Ridgecrest Earthquake Sequence (California, USA, 2019)** | High-resolution aftershock data from the 2019 M7.1 earthquake recorded on dark fiber. A key resource for earthquake physics and machine learning.  | [HuggingFace Link](https://huggingface.co/datasets/AI4EPS/quakeflow_das)                                                                                |
| **SISSLE Experiment (New Zealand, 2023)**             | Uses a fiber optic cable along a highway to monitor the Alpine Fault, one of the world's major plate boundaries, to characterize its structure and seismicity. | [Link](https://datacommons.anu.edu.au/DataCommons/rest/display/anudc:6317)                                                                  |
| **Rock-Slope Failure Monitoring (Switzerland, 2023)** | Combines DAS and radar data to monitor rock collapses. A unique resource for developing algorithms to detect landslide precursors.                     | [Link](https://data.europa.eu/data/datasets/8ece0152-55ca-4547-8faf-99bfa56f6b03-envidat?locale=en)                                           |
| **Event Classification (Czech Republic, 2021–2023)**  | A dataset designed for machine learning with thousands of labeled events (cars, construction, footsteps) for urban and security applications.           | [Link](https://springernature.figshare.com/articles/dataset/Comprehensive_Dataset_for_Event_Classification_Using_Distributed_Acoustic_Sensing_DAS_Systems/27004732?file=52736258) |
| **Fairbanks Permafrost Experiment (Alaska, USA, 2017)** | A dataset monitoring permafrost thaw during a controlled heating experiment using a grid of fiber cables. Includes active source (vibrator) and passive data. | [Globus Link](https://app.globus.org/file-manager?origin_id=706e304c-5def-11ec-9b5c-f9dfb1abb183&origin_path=%2FFairbanks%2F)                          |
| **FOSSA (Sacramento, California, USA, 2017–2018)**    | Data from a 27 km section of dark telecommunications fiber used to monitor regional seismicity and characterize near-surface structures using ambient noise. | [Globus Link](https://app.globus.org/file-manager?origin_id=706e304c-5def-11ec-9b5c-f9dfb1abb183&origin_path=%2FFOSSA%2F)                              |
| **LaFarge-Conco Mine (Illinois, USA, 2017)**          | Data from a limestone mine using a ~1.1 km fiber optic loop to record seismic signals from active sources (weight drops) and mine blasts.                 | [Globus Link](https://app.globus.org/file-manager?origin_id=706e304c-5def-11ec-9b5c-f9dfb1abb183&origin_path=%2FLaFarge%2F)                          |
| **Stanford Campus Arrays (California, USA, 2016–2020)** | Several datasets from fiber optic cables on and around the Stanford campus used for urban monitoring, earthquake detection, and infrastructure studies. | [Globus Link](https://app.globus.org/file-manager?origin_id=706e304c-5def-11ec-9b5c-f9dfb1abb183&origin_path=%2FStanford-1-Campus%2F&two_pane=false) |
| **Garner Valley (California, USA, 2013)**             | Data from a well-instrumented test site, used for numerous studies comparing DAS performance to traditional seismometers. Includes active source data.   | [DOI: 10.15121/1261941](https://doi.org/10.15121/1261941)                                                                                   |

> **Note**: Links are accessible as of June 26, 2025. For some repositories, you may need to register an account (e.g., Globus).

*Credit: A significant portion of this list was compiled from the paper "PubDAS: A PUBlic Distributed Acoustic Sensing Datasets Repository for Geosciences" by Spica et al. (2023), Seismological Research Letters.*
