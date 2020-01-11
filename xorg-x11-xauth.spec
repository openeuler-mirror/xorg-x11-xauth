Name:           xorg-x11-xauth
Version:        1.1
Release:        1
Epoch:          1
Summary:        X.Org X11 X authority utilities
License:        MIT
URL:            https://www.x.org
Source0:        https://www.x.org/pub/individual/app/xauth-%{version}.tar.bz2

BuildRequires: pkgconfig automake gcc libX11-devel libXau-devel
BuildRequires: libXext-devel libXmu-devel

Provides: xauth

%description
xauth is used to edit and display the authorization information
used in connecting to an X server.

%package_help

%prep
%autosetup -n xauth-%{version} -p1

%build
%configure
%make_build

%install
%make_install

%check
make check || cat tests/test-suite.log

%files
%defattr(-,root,root)
%license COPYING
%{_bindir}/xauth

%files help
%defattr(-,root,root)
%doc README.md ChangeLog
%{_mandir}/man1/xauth.1*

%changelog
* Thu Jan 09 2020 openEuler Buildteam <buildteam@openeuler.org> - 1.1-1
- Type:enhancement
- Id:NA
- SUG:NA
- DESC:update version to 1.1

* Fri Oct 11 2019 openEuler Buildteam <buildteam@openeuler.org> - 1: 1.0.9-14
- Package init
