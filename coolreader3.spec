%define		shortname	cr

Summary:	Free e-book reader
Name:		coolreader3
Version:	3.0.56
Release:	3
License:	GPLv2+
Group:		Books/Literature
Url:		http://www.coolreader.org
Source0:	%{shortname}3_%{version}.orig.tar.gz
BuildRequires:	cmake
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(Qt3Support)
BuildRequires:	pkgconfig(zlib)

%description
CoolReader 3.X is free open-source (GPL) multiplatform version under active
development.

%files
%{_bindir}/%{shortname}3
%{_datadir}/%{shortname}3/*.css
%{_datadir}/%{shortname}3/i18n/*.qm
%{_datadir}/%{shortname}3/hyph/*.pdb
%{_datadir}/%{shortname}3/hyph/*.pattern
%{_datadir}/%{shortname}3/textures/*.jpg
%{_datadir}/%{shortname}3/backgrounds/*.jpg
%{_datadir}/pixmaps/%{shortname}3.*
%{_datadir}/applications/%{shortname}3.desktop
%{_datadir}/doc/%{shortname}3/*
%{_mandir}/man1/%{shortname}3.*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{shortname}%{version}-7

%build
%cmake \
	-DGUI=QT \
	-DMAX_IMAGE_SCALE_MUL=2 \
	-DDOC_DATA_COMPRESSION_LEVEL=3 \
	-DDOC_BUFFER_SIZE=0x1400000 \
	-DCMAKE_BUILD_TYPE=Release
%make

%install
%makeinstall_std -C build

