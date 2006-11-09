Summary:	HDS - Hierarchical Data System
Summary(pl):	HDS - hierarchiczny system danych
Name:		starlink-hds
Version:	4.3_4.218
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.starlink.rl.ac.uk/pub/ussc/store/hds/hds.tar.Z
# Source0-md5:	958b8eba37e53175bc890d70257908da
URL:		http://www.starlink.rl.ac.uk/static_www/soft_further_HDS.html
BuildRequires:	gcc-g77
BuildRequires:	sed >= 4.0
BuildRequires:	starlink-chr-devel
BuildRequires:	starlink-ems-devel
BuildRequires:	starlink-sae-devel
Requires:	starlink-sae
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		stardir		/usr/lib/star

%description
HDS is a file-based hierarchical data system designed for the storage
of a wide variety of information. It is particularly suited to the
storage of large multi-dimensional arrays (with their ancillary data)
where efficient access is needed.

HDS organises data into hierarchies, broadly similar to the directory
structure of a hierarchical filing system, but contained within a
single HDS container file. The structures stored in these files are
self-describing and flexible; HDS supports modification and extension
of structures previously created, as well as deletion, copying,
renaming, etc.

All information stored in HDS files is portable between the machines
on which HDS is implemented. Thus, there are no format conversion
problems when moving between machines.

%description -l pl
HDS to oparty na plikach hierarchiczny system danych opracowany do
przechowywania ró¿nych informacji. W szczególno¶ci jest dopasowany do
przechowywania du¿ych wielowymiarowych tablic (z ich danymi
pomocniczymi), gdzie potrzebny jest wydajny dostêp.

HDS organizuje dane w hierarchie, podobnie jak struktury katalogów w
hierarchicznym systemie plików, ale zawarte w pojedynczym pliku
kontenera HDS. Struktury zapisane w tych plikach s± samoopisuj±ce siê
i elastyczne; HDS obs³uguje modyfikowanie i rozszerzanie poprzednio
utworzonych struktur, a tak¿e usuwanie, kopiowanie, zmianê nazwy itp.

Wszystkie informacje zapisane w plikach HDS s± przeno¶ne miêdzy
maszynami, na których HDS jest zaimplementowany, dlatego nie ma
problemu konwersji formatu przy przenoszeniu miêdzy maszynami.

%package devel
Summary:	Header files for HDS library
Summary(pl):	Pliki nag³ówkowe biblioteki HDS
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	starlink-chr-devel
Requires:	starlink-ems-devel

%description devel
Header files for HDS library.

%description devel -l pl
Pliki nag³ówkowe biblioteki HDS.

%package static
Summary:	Static Starlink HDS library
Summary(pl):	Statyczna biblioteka Starlink HDS
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Starlink HDS library.

%description static -l pl
Statyczna biblioteka Starlink HDS.

%prep
%setup -q -c

sed -i -e "s/-O2 /%{rpmcflags} /;s/ ld -shared -soname / g77 -shared \\\$\\\$3 -Wl,-soname=/" mk
sed -i -e "s/\\('-L\\\$(STAR\\)_LIB) /\\1LINK)\\/share /;s/-L\\\$(STAR_LIB) lib\\\$(PKG_NAME)\\.a/-L\\\$(STARLINK)\\/share -L. -l\\\$(PKG_NAME)/" makefile

%build
LD_LIBRARY_PATH=. \
PATH="$PATH:%{stardir}/bin" \
SYSTEM=ix86_Linux \
./mk build \
	STARLINK=%{stardir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{stardir}/help

SYSTEM=ix86_Linux \
./mk install \
	STARLINK=%{stardir} \
	INSTALL=$RPM_BUILD_ROOT%{stardir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc hds.news
%{stardir}/dates/*
%docdir %{stardir}/docs
%{stardir}/docs/sun*
%{stardir}/help/fac*
%attr(755,root,root) %{stardir}/share/*.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{stardir}/bin/hds_dev
%attr(755,root,root) %{stardir}/bin/hds_link*
%{stardir}/include/*

%files static
%defattr(644,root,root,755)
%{stardir}/lib/*.a
