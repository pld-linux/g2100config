Summary:	GTK+ HP LaserJet 2100 configuration tool
Summary(pl):	Narzêdzie GTK+ do konfigurowania drukarek HP LaserJet 2100
Name:		g2100config
Version:	0.5
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://download.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
URL:		http://g2100config.sourceforge.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gtk+-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description
g2100config is a GTK+ control tool for the HP LaserJet 2100 Series
printers. Current options are Resolution, Density, Courier Font, Econo
Mode, Tray Locking, and Test Page printing.

%description -l pl
g2100config to narzêdzie do konfiguracji drukarek HP LaserJet serii
2100. Aktualnie mo¿liwe do zmieniania opcje to: rozdzielczo¶æ,
gêsto¶æ, czcionka, tryb ekonomiczny, blokowanie podajników i
drukowanie strony testowej.

%package -n 2100config
Summary:	Console HP LaserJet 2100 configuration tool
Summary(pl):	Narzêdzie tekstowe do konfigurowania drukarek HP LaserJet 2100
Group:		Applications/Printing

%description -n 2100config
g2100config is a console control tool for the HP LaserJet 2100 Series
printers. Current options are Resolution, Density, Courier Font, Econo
Mode, Tray Locking, and Test Page printing.

%description -n 2100config -l pl
g2100config to narzêdzie do konfiguracji drukarek HP LaserJet serii
2100. Aktualnie mo¿liwe do zmieniania opcje to: rozdzielczo¶æ,
gêsto¶æ, czcionka, tryb ekonomiczny, blokowanie podajników i
drukowanie strony testowej.

%prep
%setup -q
%{__make} distclean
rm -f console/2100config

%build
gettextize --copy --force
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

cd console
%{__make} CFLAGS="$RPM_OPT_FLAGS" 2100config

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/usr/bin,%{_mandir}/man1}

%{__make} DESTDIR=$RPM_BUILD_ROOT install
install console/2100config $RPM_BUILD_ROOT/usr/bin
install console/2100config.1 $RPM_BUILD_ROOT%{_mandir}/man1
gzip -9nf AUTHORS NEWS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%files -n 2100config
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/*
%{_mandir}/man1/*
