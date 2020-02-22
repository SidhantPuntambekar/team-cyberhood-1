---
title: "Pcap capture file source"
permalink: /docs/readme/datasources_pcapfile/
excerpt: "Pcap datasources replay existing pcap files as if they were live data"
docgroup: "readme"
toc: true
---

## Replaying data
Kismet can replay recorded data in the `pcap` and `pcap-ng` formats.  Pcap files are commonly generated by tools like `tcpdump`, `wireshark`, `tshark`, and Kismet itself.

Kismet can replay a pcapfile for testing, debugging, demo, or reprocessing.

### Datasource - Pcapfile

The Pcapfile datasource will auto-detect pcap files and paths to files:
```bash
$ kismet -c /tmp/foo.pcap
```

It can be manually specified with `type=pcapfile`, as in:

```source=/tmp/foo.pcap:type=pcapfile```

The pcapfile capture uses the 'kismet_cap_pcapfile' tool which does not need special privileges.

Currently Kismet supports pcap-ng files with a single interface in the capture; multi-interface captures will appear as coming from a single data source - that of the pcapfile itself.

### Pcapfile Options
In addition to the normal options supported by all sources (name, information elements, UUID, etc) the pcapfile source can also support:

* `pps=rate`
   Normally, pcapfiles are replayed as quickly as possible.  On larger pcaps this can lead to CPU and RAM contention, and dropped packets.  Specifying a packets-per-second rate throttles processing of the packet to a more sustainable speed.
   This option cannot be combined with the `realtime` option.

* `realtime=true | false`
   Normally, pcapfiles are replayed as quickly as possible.  On larger pcaps this can lead to CPU and RAM contention, and dropped packets.  Specifying `realtime=true` in your source definition will reduce the packet processing rate to the original capture rate, and the packets will be processed with real-time delays equal to how they were received.
   
 These options can be used in the kismet.conf and kismet_site.conf, as in:
 
 ```source=/tmp/foo.pcap:type=pcapfile,name=a_meaningful_name,realtime=true```
 
 Or from the command line:
 
 ```bash
$ kismet -c /tmp/foo.pcap:name=a_meaningful_name,pps=1000
```
 
 
