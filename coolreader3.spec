%define		shortname	cr

Summary:	Free e-book reader
Name:		coolreader3
Version:	3.2.51
Release:	1
License:	GPLv2+
Group:		Books/Literature
URL: https://sourceforge.net/projects/crengine
Source0: https://github.com/buggins/coolreader/archive/cr%{version}/coolreader-cr%{version}.tar.gz

BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: pkgconfig(fontconfig)
BuildRequires: pkgconfig(libpng)
BuildRequires: pkgconfig(zlib)
BuildRequires: pkgconfig(libjpeg)
BuildRequires: pkgconfig(fribidi)
BuildRequires: pkgconfig(freetype2)
BuildRequires: pkgconfig(harfbuzz)
#BuildRequires: pkgconfig(libunibreak)
BuildRequires: cmake(Qt5Core)
BuildRequires: cmake(Qt5Gui)
BuildRequires: cmake(Qt5LinguistTools)


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
%autosetup -n coolreader-cr%{version}

%build
%cmake \
	-DGUI=QT5 \
  	-DCMAKE_BUILD_TYPE=Release \
  	-DMAX_IMAGE_SCALE_MUL=2 \
  	-DDOC_DATA_COMPRESSION_LEVEL=3 \
  	-DDOC_BUFFER_SIZE=0x1400000 \
  	-D CMAKE_INSTALL_PREFIX=/usr
	
%make_build

%install
%make_install -C build

