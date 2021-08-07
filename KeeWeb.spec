%define __requires_exclude libffmpeg.so

Name:    KeeWeb
Version: 1.18.7
Release: 1%{?dist}
Summary: Free cross-platform password manager compatible with KeePass
URL:     https://github.com/keeweb/keeweb
License: MIT
BuildRequires: desktop-file-utils

Source0: https://github.com/keeweb/keeweb/releases/download/v%{version}/KeeWeb-%{version}.linux.x64.zip
Source1: %{name}.desktop


%description
Free cross-platform password manager compatible with KeePass

%prep
%autosetup -c KeeWeb-%{version}

%install
mkdir -p %{buildroot}/opt
cp -r ../KeeWeb-%{version} %{buildroot}/opt/KeeWeb
install -m 0644 -D %{SOURCE1} %{buildroot}%{_datadir}/applications/KeeWeb.desktop
#desktop-file-validate %{buildroot}%{_datadir}/applications/KeeWeb.desktop

%files
/opt/KeeWeb/*
%{_datadir}/applications/KeeWeb.desktop