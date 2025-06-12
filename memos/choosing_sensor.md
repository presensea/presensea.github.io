# Feeling the Pressure? A Deep Dive into Low-Cost Underwater Sensors

Make vs. Buy: Cost-Effective Underwater Pressure Sensors for DIY & Research Projects

When you need to measure pressure underwater, the first question is always: Do you build it yourself, or buy a ready-made solution? Sure, companies like Blue Robotics, Keller, or Impact Sea sell pre-sealed, high-reliability sensors. But if your project operates under tight budget constraints—or prioritizes hands-on prototyping for research and development—buying off-the-shelf solutions might leave you high and dry. Let’s explore your options and dive into practical alternatives!

Some MEMS shops like [Mouser](https://www.mouser.ee/c/sensors/pressure-sensors/) or DigiKey offer a comprehensive characteristic filter for choosing between thousands of different sensors. Let’s chart a course through the options and avoid drowning in complexity.

How to Choose Underwater Pressure Sensors: Key Questions for Accurate Data Collection

The choice is obviously defined by specific application, in research it can be very different. But at this point let’s ask the right questions.

- What is the data?
  - Hydrostatic that is dependent on the depth. Hydrodynamic – small fluctuations of the pressure that may come from moving pressure media (or vessel itself). Acoustic pressure is a whole another application which we will not consider in this post.
- What are the environment requirements?
  - Freshwater or saltwater? Will it face mechanical vibrations, EMI/RFI interference, or the wrath of Neptune himself?
- What are the design requirements?
  - how the sensor will be sealed? Will you use digital or analog signals? What connector works best?

### What data do you want to measure?

While there is a lot of different sources for underwater pressure, there are always two components. Hydrostatic that is dependent on the depth. Hydrodynamic – small fluctuations of the pressure that may come from moving pressure media (or vessel itself). Acoustic pressure is a whole another source which we will not consider in this post.

When it comes to how we measure, we can measure absolute pressure (relative to perfect vacuum), gauge (relative to some value e.g. ambient atmospheric pressure) and differential (difference between pressure in two points). For underwater environment, make sure that gauge sensors have properly sealed gauge port.

Many sensors types are prone to temperature errors so many add temperature measurement and compensation \[1\]. Think of integration of additional sensors (e.g. conductivity or full AHRS) if needed.

How accurate and frequent we want the data to be?

### Sensor Types Compared: Piezoresistive, Capacitive, and Fiber-Optic for Underwater Use

This should define the physical principle behind the sensor. Here is a table with some basic information.

| Type of sensor | Principle | Pro | Contras |
| --- | --- | --- | --- |
| Piezoresistive \[1, 2\] | Electrical resistance of material is changed when exposed to pressure. | Mature, Low cost, widely used, high sensitivity (sub-Pascal resolution) | Sensitive to temperature induced errors, in harsh medias prone to long term drift and hysteresis. |
| Capacitive \[3, 4\] | Two parallel conductive plates, one of them is a flexible diaphragm that deforms under pressure and changes the capacitance | Mature, no DC power, long-term and overpressure stability, | Require complex low-noise interface and calibration algorithms, silicon components suffer from salt exposure |
| Stain Gauge | Like piezoresistive technology, but the resistance element is spring-like that deforms under pressure | More suitable for long-term monitoring |     |
| Piezoelectric \[6, 7\] | Ceramic or polymer material generates a charge under pressure | Robust, no DC power, high sensitivity to fast small pressure pulses in MHz range | Output charge leaks so can only measure dynamic (AC) pressure changes |
| Fiber-optic \[8\] | Measures strain-induced wavelength shift | No DC power, Immune to electromagnetic interference, potentially tens of kHz response, naturally corrosion proof | Emerging \\ Requires costly laser interrogators |
| Flexible polymer \[9\] | Porous composites | high sensitivity to constant pressure | Emerging, slow (tens of Hz) due to viscoelasticity, |

### Environmental Challenges: Corrosion, Biofouling, and Pressure Protection for Sensors

Underwater environment is harsh. While some sensors offer waterproof capabilities out of the box, for critical applications, long-term deployments or deep ocean, any sensor may need pressure housing, oil filling or other types of encapsulation.

Even if you need a non-critical and short term deployment, you still need to consider a design that will stand corrosion (especially in salty water) and leaking. When it comes to long term, the design should withstand not only pressure, but also biofouling and internal condensation. Organic materials of sensor membranes and sealing after long exposure may start leaking or giving wrong results.

**Pressure equalization**. Even for small depth air-tight seals when exposed to temperature and pressure change may be stressed and leaking. Consider pressure compensation elements (vent holes) for critical designs.

**Corrosion** and biofouling in salty water is particularly aggressive. Choose stainless steel alloys for sensor housing, and titanium for extra-long term and harsh conditions \[2\]. Protect connections (e.g. o-rings) using specialized polymer compounds (e.g. PVDF or PTFE), for extra protection using welded seals and all-metal design. The board and other MEMS components are recommended to cover with conformal coating or some encapsulation (make sure the ports are still exposed to pressure media). For fast prototyping acrylic or silicon coating can be brushed or sprayed over (and removed if needed). Epoxy/Parylene dipping can offer a longer protection \[10\].

When you want to seal your sensor on your own, make sure the sensor and it’s components is able to withstand any associated process (solvents in conformal coatings, curing temperature of putting compounds etc.) Also make sure that the sensing element (or port) is properly

Analog vs. Digital Sensors: Signal Integrity for Underwater Pressure Monitoring

Analog signal (e.g. voltage or current loop) is continuous which may be crucial for some real-time applications. However analog voltage signal is prone to noise especially in long cables. It also may require extra analog-to-digital conversion and signal processing units. Digital sensors already include A2D conversion and often some basic signal processing units \[11\]. However the output is quantized which may be an issue when sensor is intended for high depth and exact low depth values are needed.

### Top Low-Cost Underwater Sensors: Depth Range, Accuracy & Compatibility Guide

| Sensor | Protection type | Depth range | Output | Size | Price (EUR) | Datasheet |
| --- | --- | --- | --- | --- | --- | --- |
| Bosch Sensortec BMP384 | Gel-filled | Barometric (~2.5m) | Digital (I2C/SPI) | 2.0 x 2.0 x 1.0 mm | 2-4 | [Link](https://www.bosch-sensortec.com/media/boschsensortec/downloads/datasheets/bst-bmp384-ds001.pdf) |
| STMicroelectronics LPS27HHTW | WR package, potting gel, o-ring compatible | Barometric (~2.6m) | Digital (I2C/SPI/I3C) | 2.5 x 2.5 x 1.1 mm | 3-6 | [Link](https://www.st.com/resource/en/datasheet/lps27hhtw.pdf) |
| STMicroelectronics ILPS28QSWTR | WR package, potting gel, Qvar | Up to 40m | Digital (I2C, 24 bit) | 2.8 x 2.8 x 1.95 mm | 5-7 | [Link](https://www.st.com/resource/en/datasheet/ilps28qsw.pdf) |
| TE Connectivity MS5837 | Gel-filled, protective cap | Up to 300m | Digital (I2C, 24 bit) | 3.3 x 3.3 x 2.75 mm | 10-15 | [Link](https://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7FMS5837-30BA%7FB3%7Fpdf%7FEnglish%7FENG_DS_MS5837-30BA_B3.pdf%7FCAT-BLPS0036) |
| TE Connectivity EPB-PW | Titanium housing, sealed gauge | High pressure | Analog (mV/V) | 6.4mm x 11.4mm | ~200 | [Link](https://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7FEPB-PW%7FB%7Fpdf%7FEnglish%7FENG_DS_EPB-PW_B.pdf%7FCAT-PTT0004) |
| TE Connectivity AST4530 | Stainless steel housing, sealed | Up to 700m | Analog (V, mA) | ~25.4mm diameter | 150-400 | [Link](https://www.te.com/commerce/DocumentDelivery/DDEController?Action=showdoc&DocId=Data+Sheet%7FAST4530%7FE%7Fpdf%7FEnglish%7FENG_DS_AST4530_E.pdf%7F11108534-00) |
| Honeywell HSC/SSC (liquid) | Liquid media option | Up to 100m | Analog, Digital | ~10 x 10 mm | 20-70 | [Link](https://prod-edam.honeywell.com/content/dam/honeywell-edam/sps/siot/en-us/products/sensors/pressure-sensors/board-mount-pressure-sensors/trustability-hsc-series/documents/sps-siot-trustability-hsc-series-high-accuracy-datasheet-32300898-ciid-150252.pdf) |
| Honeywell SPT series | Stainless steel wetted part | Up to 3450m | Analog (mV, V, mA) | ~22mm diameter | 70-200 | [Link](https://www.farnell.com/datasheets/1562902.pdf) |
| Honeywell MIP series | Stainless steel, Sealed (IP67) | Up to 600m | Analog, Digital (SENT) | ~27mm hex body | 80-250 | [Link](https://prod-edam.honeywell.com/content/dam/honeywell-edam/sps/siot/en-us/products/sensors/pressure-sensors/media-isolated-pressure-sensors/mip-series/documents/sps-siot-mip-series-datasheet-008230-6-en-ciid-150247.pdf) |
| Honeywell PX2 series | Stainless steel, Sealed (IP69K) | Up to 700m | Analog, Digital (CAN) | ~25mm hex body | 100-300 | [Link](https://prod-edam.honeywell.com/content/dam/honeywell-edam/sps/siot/en-us/products/sensors/pressure-sensors/heavy-duty-pressure-transducers/px2-series/documents/sps-siot-px2-series-datasheet-32328127-d-en-ciid-150249.pdf) |
| NXP NBP 8/9X | Chemical resistant gel | Barometric (not for depth) | Digital (SPI, PWM) | 4 x 4 mm | 10-25 | [Link](https://www.nxp.com/docs/en/data-sheet/NBP8-9X.pdf) |
| Adafruit LPS28DFW | WR pkg (board needs sealing) | Up to 40m | Digital (I2C) | 25.4 x 17.8 mm | 12-15 | [Link](https://www.adafruit.com/product/6067) |
| Adafruit LPS33HW | WR pkg (board needs sealing) | Up to 2.5m | Digital (I2C/SPI) | 25.4 x 17.8 mm | 12-15 | [Link](https://www.adafruit.com/product/4414) |
| Blue Robotics Bar30 | Sealed unit, o-ring mount | Up to 300m | Digital (I2C) | 20mm dia, 26mm len | 80-100 | [Link](https://bluerobotics.com/wp-content/uploads/2021/10/Bar30-Datasheet-Rev4.pdf) |

\*Prices are valid as of 12.06.25

### **Sealing Techniques: Protecting Underwater Sensors from Leaks and Condensation**

When safeguarding underwater sensors, conformal coatings like brush-on or sprayed acrylic or silicone offer a lightweight, removable shield for short-term deployments—a flexible solution for prototyping or temporary setups. For more permanent installations, epoxy or parylene encapsulation acts as a "suit of armor," providing robust, long-term defense against moisture and corrosion. However, always verify material compatibility : Ensure seals and coatings withstand curing temperatures, solvents, or mechanical stress during assembly. For rapid prototyping, consider unconventional methods like sealing sensors in balloons—a low-cost, DIY approach highlighted in projects like [MIT SeaPerch’](https://seagrant.mit.edu/seaperch2-pressure/)s pressure-testing guide . Balancing protection, durability, and ease of implementation ensures your sensor survives both lab trials and real-world depths.

### References

1. Vardanyan, Y., & Pyo, S. (2024). Emerging MEMS sensors for ocean physics: Principles, materials, and applications. APL Machine Learning, 2(2), 020901.
2. Barlian, A. A., et al. (2007). Review: Semiconductor Piezoresistance for Microsystems. Proceedings of the IEEE, 97(3), 513-552.
3. Ko, W. H., & Wang, Q. (1998). Touch mode capacitive pressure sensors. Sensors and Actuators A: Physical, 75(3), 242-251.
4. Fraden, J. (2016). Handbook of Modern Sensors: Physics, Designs, and Applications. Springer.
5. Puers, R. (2010). Linking capacitive sensors to the digital world. Procedia Engineering, 5, 68-75.
6. Avnet Abacus. "Capacitive vs Piezoresistive vs Piezoelectric Pressure Sensors." URL: &lt;<https://my.avnet.com/abacus/solutions/technologies/sensors/pressure-sensors/core-technologies/capacitive-vs-piezoresistive-vs-piezoelectric/>&gt;
7. PCB Piezotronics. "Introduction to Piezoelectric Pressure Sensors." URL: &lt;<https://www.pcb.com/resources/technical-information/introduction-to-pressure-sensors>&gt;
8. Bai, W., et al. (2022). Submarine Optical Fiber Sensing System for the Real-Time Monitoring of Depth, Vibration, and Temperature. Frontiers in Marine Science, 9.
9. Lee, H., et al. (2015). Development of a porous piezoresistive material and its applications to underwater pressure sensors and tactile sensors. 2015 IEEE SENSORS.
10. ELEPCB. "The Ultimate Guide to Conformal Coating for Circuit Boards." URL: &lt;<https://www.elepcb.com/blog/choose-the-right-pcb-conformal-coating/>&gt;
11. xidibei. "Is A Pressure Sensor Analog Or Digital?" URL: &lt;<https://www.xidibei.com/blogs/news/is-a-pressure-sensor-analog-or-digital>&gt;
