---
title: "Remote capture"
permalink: /docs/readme/datasources_remote_capture/
excerpt: "Remote network capture allows Kismet to receive packets from distributed sensors installed on other hardware, such as OpenWRT routers."
docgroup: "readme"
toc: true
---

## Remote Packet Capture
Kismet can capture from a remote source over a TCP connection.

Kismet remote packet feeds are initiated by the same tools that Kismet uses to configure a local source; for example if Kismet is running on a host on IP 192.168.1.2, to capture from a Linux Wi-Fi device on another device you would use:

```bash
# kismet_cap_linux_wifi --connect 192.168.1.2:3501 --source=wlan1
```

Specifically, this uses the `kismet_cap_linux_wifi` tool, which is by default installed in `/usr/local/bin/`, to connect to the IP `192.168.1.2` port 3501.

The --source=... parameter is the same as you would use in a `source=` Kismet configuration file entry, or as `-c` to Kismet itself. 

Source definitions of a remote capture are controlled the same way as `source=` definitions in the Kismet config, and can take the same options.  It's not uncommon to have many remote captures using `wlan0` as the capture interface, but by passing the `name=foo` option to the source, it's easy to differentiate:

```bash
# kismet_cap_linux_wifi --connect 192.168.1.2:3501 --source=wlan1:name=sensor_foo_wlan1,add_channels=\"6W5,36W5\",info_antenna_type=omni
```

### Any-to-Any

Kismet is designed to allow any source to function as a remote capture, and to function cross-platform.  It is completely reasonable, for instance, to use an OpenWRT sensor running Linux to provide packets to a Kismet server running on OSX or Windows 10 under the WSL.

### Controlling access to remote capture

For security reasons, by default Kismet only accepts remote sensor connections from the localhost IP (`127.0.0.1`).  To connect remote sensors, you must either:

1. Set up a tunnel from the remote sensor to your Kismet server, for example using SSH port forwarding.  This is very simple to do, and adds encryption transparently to the remote packet stream.  This can be done as simply as:

   ```bash
   # ssh someuser@192.168.1.2 -L 3501:localhost:3501
   ```

   This sets up a SSH tunnel from `localhost` port 3501 to `192.168.1.2` port 3501.  Then in a second terminal running the Kismet remote capture, using `localost:3501` as the destination:

   ```
   # /usr/local/bin/kismet_cap_linux_wifi --connect localhost:3501 --source=wlan1
   ```

   Other, more elegant solutions exist for building the SSH tunnel, such as `autossh` which can be used to automatically maintain the tunnel and start it on boot.

2.  Kismet can be configured to accept connections on a specific interface, or from all IP addresses, by changing the `remote_capture_listen=` line in `kismet.conf` or `kismet_site.conf` as an override.  To enable listening on ALL network interfaces:

   ```
   remote_capture_listen=0.0.0.0
   ```

   Or a single specific network interface:
   ```
   remote_capture_listen=192.168.1.2
   ```

   Remote capture *should only be enabled on interfaces on a protected LAN*.

### Additional remote capture options

Kismet capture tools also support the following options:

* `--connect=[host]:[port]`
   Connects to a remote Kismet server on [host] and port [port].  When using `--connect=...` you MUST specify a `--source=...` option

* `--source=[source definition]`
   Define a source; this is used only in remote connection mode.  The source definition is the same as defining a local source for Kismet via `-c` or the `source=` config file option.

* `--disable-retry`
   By default, a remote source will attempt to reconnect if the connection to the Kismet server is lost.

* `--daemonize`
   Places the capture tool in the background and daemonizes it.

* `--fixed-gps [lat,lon,alt] or [lat,lon]`
   Set the GPS location of the remote capture source; this will tag any packets from this source with a static, fixed GPS location.

* `--gps-name [name]`
   Rename the virtual GPS reported on this source; otherwise the capture name "fixed-remote" is used.

### Filtering remote-capture Wi-Fi

Remote capture is designed to be as lightweight as possible and does not process packet contents, however it can still support BPF filtering.  When doing a remote Wi-Fi capture on a dual-radio capture platform connected over Wi-Fi itself, the remote capture stream will often see itself transmitting packets to the Kismet server, leading to a huge bandwidth spike and loop.

By specifying the `filter_locals=true` source option, `kismet_cap_linux_wifi` will automatically build a BPF filter to exclude all local interfaces found on the system:

```bash
# kismet_cap_linux_wifi --connect some-kismet-server:3501 --source wlan0:name=some_remote_cap,filter_locals=true
```

Because the Linux kernel has a limited amount of space for BPF filter programs, only the first *eight* interfaces found on the system are included in the BPF filter, currently.

### Remote capture timestamps

By default, Kismet will override the packet timestamp from a remote capture with the timestamp of *when the packet is seen by the Kismet server*.  Otherwise, variance in the clocks of remote captures can cause problems with Kismet - such as invalid WIDS alerts - due to some packets arriving "in the past".

If your clocks are synced with NTP, or if you want to preserve the timestamp for some other reason, you can use the source option `timestamp=false`:

```bash
# kismet_cap_linux_wifi --connect some-kismet-server:3501 --source wlan0:name=some_remote_cap,timestamp=false
```

### Compiling Only the Capture Tools

Typically, you will want to compile all of Kismet.  If you're doing specific remote-capture installs, however, you may wish to compile only the binaries used by Kismet to enable capture mode and pass packets to a full Kismet server.

To compile ONLY the capture tools:

Tell configure to only configure the capture tools; this will allow you to configure without installing the server dependencies such as C++, microhttpd, protobuf-C++, etc.  You will still need to install dependencies such as protobuf-c, build-essentials, and similar:
```bash
$ ./configure --enable-capture-tools-only
```

Once configure has completed, compile the capture tools:
```bash
$ make datasources
```

You can now copy the compiled datasources to your target.

