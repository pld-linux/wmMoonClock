Name:		wmMoonClock
Summary:	Moon phases info for Window Maker/AfterStep
Summary(pl):	Informacja o fazach ksiê¿yca dla WindowMakera/AfterStepa
Version:	1.1
Release:	2
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Copyright:	GPL
Source0:	ftp://leadbelly.lanl.gov/pub/mgh/%{name}-%{version}.tar.gz
Source1:	wmMoonClock.wmconfig
Icon: 		wmMoonClock.gif
BuildRoot:	/tmp/%{name}-%{version}-root

%description
wmMoonClock displays the current phase of the moon.  
Window Maker and AfterStep dockable but not necessary.

%description -l pl
wmMoonClock wy¶wietla aktualn± fazê ksiê¿yca. 
Dokowalny w WindowMakerze i AfterStepie, lecz nie jest to koniecznie.

%prep
%setup -q 

%build
make -C wmMoonClock CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/X11R6/{bin,man/man1}}
make -C wmMoonClock install DESTDIR=$RPM_BUILD_ROOT/usr/X11R6/

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/wmMoonClock

gzip -9nf $RPM_BUILD_ROOT/usr/X11R6/man/man1/wmMoonClock.1

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/X11R6/bin/wmMoonClock
/usr/X11R6/man/man1/wmMoonClock.1.gz

%config(missingok) /etc/X11/wmconfig/wmMoonClock

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Mon Mar 23 1999 Piotr Czerwiñski <pius@pld.org.pl>
  [1.1-2]
- removed binary files from sources,
- typos in man page corrected,
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
