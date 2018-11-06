## SuperWASP dashboard preview generation daemon [![Travis CI build status](https://travis-ci.org/warwick-one-metre/wasp-previewd.svg?branch=master)](https://travis-ci.org/warwick-one-metre/wasp-previewd)

Part of the observatory software for the Warwick La Palma observatory.

`wasp-previewd` copies frames from the SuperWASP dataloader and generates a png preview of the central four cameras for the web dashboard.

`wasp-preview` is a commandline utility that is called over `ssh` to notify of a new frame.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.

### Software setup

After installing `wasp-preview-server`, the `previewd` must be enabled using:
```
sudo systemctl enable wasp-previewd.service
```

The service will automatically start on system boot, or you can start it immediately using:
```
sudo systemctl start wasp-previewd.service
```

The service runs locally, so the firewall does not need to be modified.

The daemon assumes that it is running on the same host as the dashboard, and will write directly into the generated file directory instead of using a nfs mount.
