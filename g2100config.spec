Summary:	GTK+ HP LaserJet 2100 configuration tool
Summary(pl.UTF-8):	Narzędzie GTK+ do konfigurowania drukarek HP LaserJet 2100
Name:		g2100config
Version:	0.5
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	9d07233734404ebd44bc06a8b1928b14
URL:		http://g2100config.sourceforge.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	gettext-tools
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
g2100config is a GTK+ control tool for the HP LaserJet 2100 Series
printers. Current options are Resolution, Density, Courier Font, Econo
Mode, Tray Locking, and Test Page printing.

%description -l pl.UTF-8
g2100config to narzędzie do konfiguracji drukarek HP LaserJet serii
2100. Aktualnie możliwe do zmieniania opcje to: rozdzielczość,
gęstość, czcionka, tryb ekonomiczny, blokowanie podajników i
drukowanie strony testowej.

%package -n 2100config
Summary:	Text-mode HP LaserJet 2100 configuration tool
Summary(pl.UTF-8):	Narzędzie tekstowe do konfigurowania drukarek HP LaserJet 2100
Group:		Applications/Printing

%description -n 2100config
2100config is a text-mode control tool for the HP LaserJet 2100 Series
printers. Current options are Resolution, Density, Courier Font, Econo
Mode, Tray Locking, and Test Page printing.

%description -n 2100config -l pl.UTF-8
2100config to tekstowe narzędzie do konfiguracji drukarek HP LaserJet
serii 2100. Aktualnie możliwe do zmieniania opcje to: rozdzielczość,
gęstość, czcionka, tryb ekonomiczny, blokowanie podajników i
drukowanie strony testowej.

%prep
%setup -q
%{__make} distclean
rm -f console/2100config

%build
rm -f missing
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

cd console
%{__make} 2100config \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/usr/bin,%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install console/2100config $RPM_BUILD_ROOT/usr/bin
install console/2100config.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%files -n 2100config
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/*
%{_mandir}/man1/*
