Name:		wmMoonClock
Summary:	Moon phases info for Window Maker/AfterStep
Summary(pl):	Informacja o fazach ksi�yca dla WindowMakera/AfterStepa
Version:	1.1
Release:	4
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Copyright:	GPL
Source0:	ftp://leadbelly.lanl.gov/pub/mgh/%{name}-%{version}.tar.gz
Source1:	wmMoonClock.wmconfig
Patch0:		wmMoonClock-man.patch
Icon: 		wmMoonClock.gif
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix         /usr/X11R6

%description
wmMoonClock displays the current phase of the moon.  
Window Maker and AfterStep dockable but not necessary.

%description -l pl
wmMoonClock wy�wietla aktualn� faz� ksi�yca. 
Dokowalny w WindowMakerze i AfterStepie, lecz nie jest to koniecznie.

%prep
%setup -q 
%patch0 -p1

%build
make -C %{name} clean
make -C %{name} \
	COPTS="$RPM_OPT_FLAGS -I/usr/X11R6/include"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
        $RPM_BUILD_ROOT/etc/X11/wmconfig

install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}/%{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_mandir}/man1/*

/etc/X11/wmconfig/%{name}

%changelog
* Mon May 17 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [1.1-4]
- added more rpm macros,
- package is now FHS 2.0 compliant.

* Tue Apr 20 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [1.1-3]
- added BuildPrereq: XFree86-devel,
- recompiled on rpm 3,
- cosmetics.

* Fri Mar 26 1999 Piotr Czerwi�ski <pius@pld.org.pl>
  [1.1-2]
- added wmMoonClock-man.patch,
- added make clean before make by Artur Frysiak <wiget@pld.org.pl>,
- fixed passing $RPM_OPT_FLAGS by Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>,
- minor changes.

* Mon Mar 23 1999 Piotr Czerwi�ski <pius@pld.org.pl>
- changed Group to X11/Window Managers/Tools,
- added Buildroot,
- added -q %setup parameter,
- added using $RPM_OPT_FLAGS during compile,
- fixed %build and %install,
- added gzipping man pages,
- added full %defattr description,
- changes in %files,
- moved %changelog at the end of spec,
- major changes.
 
* Thu Dec 31 1998 Yeechang Lee <ylee@columbia.edu>
- Added wmconfig file.
