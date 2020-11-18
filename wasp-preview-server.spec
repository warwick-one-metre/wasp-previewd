Name:      wasp-preview-server
Version:   1.4.0
Release:   0
Url:       https://github.com/warwick-one-metre/wasp-previewd
Summary:   Frame preview server for the SuperWASP telescope
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires: wasp-preview-server-data
Requires: python3, python3-Pyro4, python3-astropy, python3-numpy, python3-pillow, python3-sep, python3-warwick-observatory-common

%description

Part of the observatory software for the Warwick La Palma observatory.

wasp-previewd copies frames from the SuperWASP dataloader and generates a png preview of the central four cameras for the web dashboard.

%build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_unitdir}

%{__install} %{_sourcedir}/wasp-previewd %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/wasp-previewd.service %{buildroot}%{_unitdir}

%post
%systemd_post wasp-previewd.service

%preun
%systemd_preun wasp-previewd.service

%postun
%systemd_postun_with_restart wasp-previewd.service

%files
%defattr(0755,root,root,-)
%{_bindir}/wasp-previewd
%defattr(0644,root,root,-)
%{_unitdir}/wasp-previewd.service

%changelog
