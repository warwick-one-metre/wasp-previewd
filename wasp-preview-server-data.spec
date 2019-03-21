Name:      wasp-preview-server-data
Version:   1.0.0
Release:   0
Url:       https://github.com/warwick-one-metre/wasp-previewd
Summary:   Calibration frames for wasp-preview-server
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch

%description

Calibration frames for wasp-preview-server

%build
mkdir -p %{buildroot}%{_sysconfdir}/wasp-previewd/

%{__install} %{_sourcedir}/data/*.fits.gz %{buildroot}%{_sysconfdir}/wasp-previewd/

%files
%defattr(0644,root,root,-)
%{_sysconfdir}/wasp-previewd/*.fits.gz

%changelog
