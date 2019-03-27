Name:      wasp-preview-client
Version:   1.3.0
Release:   0
Url:       https://github.com/warwick-one-metre/wasp-previewd
Summary:   Commandline utility to notify the preview daemon of a new frame to process.
License:   GPL-3.0
Group:     Unspecified
BuildArch: noarch
Requires:  python36, python36-Pyro4, python36-warwick-observatory-common

%description

Part of the observatory software for the Warwick La Palma observatory.

wasp-preview is a commandline utility that is called over `ssh` to notify of a new frame.

%build
mkdir -p %{buildroot}%{_bindir}
%{__install} %{_sourcedir}/wasp-preview %{buildroot}%{_bindir}

%files
%defattr(0755,root,root,-)
%{_bindir}/wasp-preview

%changelog
