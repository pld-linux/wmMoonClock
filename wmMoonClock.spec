Name:		wmMoonClock
Summary:	Moon phases info for Window Maker/AfterStep
Summary(pl):	Informacja o fazach ksiê¿yca dla WindowMakera/AfterStepa
Version:	1.26
Release:	2
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Copyright:	GPL
Source0:	ftp://leadbelly.lanl.gov/pub/mgh/%{name}-%{version}.tar.gz
Source1:	wmMoonClock.desktop
Icon: 		wmMoonClock.gif
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6
%define _mandir %{_prefix}/man

%description
wmMoonClock displays the current phase of the moon.  
Window Maker and AfterStep dockable but not necessary.

%description -l pl
wmMoonClock wy¶wietla aktualn± fazê ksiê¿yca. 
Dokowalny w WindowMakerze i AfterStepie, lecz nie jest to koniecznie.

%prep
%setup -q 

%build
make -C Src \
	CFLAGS="$RPM_OPT_FLAGS -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
        $RPM_BUILD_ROOT/etc/X11/applnk/DockApplets

install -s Src/%{name} $RPM_BUILD_ROOT%{_bindir}
install Src/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/DockApplets

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*

/etc/X11/applnk/DockApplets/wmMoonClock.desktop

%changelog
* Mon May 24 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [1.26-1]
- updated to 1.26,
- removed wmMoonClock-man.patch,
- some cleanups.

* Mon May 17 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.1-4]
- package is FHS 2.0 compliant,
- based on spec file written by Yeechang Lee <ylee@columbia.edu>,
  rewritten for PLD use by me, Artur Frysiak <wiget@pld.org.pl>
  and Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>.
