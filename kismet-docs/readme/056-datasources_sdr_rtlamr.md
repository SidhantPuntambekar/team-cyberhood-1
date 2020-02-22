---
title: "SDR rtlamr sources"
permalink: /docs/readme/datasources_sdr_rtlamr/
excerpt: "SDR-based rtlamr sources use the rtl-sdr radio to capture AMR based power and water meter readings."
docgroup: "readme"
toc: true
---

*Updated for Kismet 2019-10*

## RTL-AMR

To capture AMR with Kismet, you'll need a rtl-sdr USB software defined radio.  You can't capture these signals with a Wi-Fi card; they're very different!

Using a rtl-sdr, Kismet is able to capture the usage readings from AMR-enabled meters.  These often include electricity, water, and gas meters.  The AMR broadcast is used as part of the meter reading system which allows the utility company to read power usage from the street.

### Datasource - SDR RTLAMR

You will need a python3 environment and the `numpy` package, either installed via `pip3` or as a system package.

The rtlamr datasource will auto-detect supported rtl-sdr hardware.  It can be manually specified with `type=rtlamr`.

If you have multiple rtl-sdr radios, you can select which radio to use either by radio number (the order it was seen on your system), or by the serial number of the radio; for instance:

```
source=rtlamr-0,name=FirstRadio
```

or

```
source=rtlamr-124334,name=SomeOtherRadio
```

#### Rtl AMR Source Parameters
RTLAMR sources accept several additional options, in addition to the standard name, informational, and UUID options:

* `biastee=true | false`

    Enable bias-tee power on supported radios.  Bias-tee is used to supply power to external amplifiers or other equipment in the antenna chain, and requires your radio have support for it.

* `channel=frequency_in_hz`

    Manually force a different frequency; by default the standard of 912.6MHz is used.

* `gain=value`

    Specifiy a fixed gain level for the radio; by default, the hardware automatic gain control is used.

* `ppm=error_value`

    Specify a PPM error offset for fine-tuning your radio, if your hardware has a known offset.

