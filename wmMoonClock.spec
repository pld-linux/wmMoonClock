Summary:	Moon phases info for Window Maker/AfterStep
Summary(pl.UTF-8):   Informacja o fazach księżyca dla WindowMakera/AfterStepa
Name:		wmMoonClock
Version:	1.27
Release:	5
License:	GPL v2
Group:		X11/Window Managers/Tools
Source0:	http://nis-www.lanl.gov/~mgh/WindowMaker/%{name}-%{version}.tar.gz
# Source0-md5:	c85bc974e70c867d556805505d3be48c
Source1:	%{name}.desktop
URL:		http://nis-www.lanl.gov/~mgh/WindowMaker/DockApps.shtml
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmMoonClock displays the current phase of the moon. Window Maker and
AfterStep dockable but not necessary.

%description -l pl.UTF-8
wmMoonClock wyświetla aktualną fazę księżyca. Dokowalny w
WindowMakerze i AfterStepie, lecz nie jest to koniecznie.

%prep
%setup -q

%build
%{__make} -C Src \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_desktopdir}/docklets

install Src/%{name} $RPM_BUILD_ROOT%{_bindir}
install Src/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*
%{_desktopdir}/docklets/wmMoonClock.desktop
