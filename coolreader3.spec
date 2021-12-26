%define		shortname	cr

Summary:	Free e-book reader
Name:		coolreader3
Version:	3.2.58
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
BuildRequires: cmake(Qt5Widgets)
BuildRequires: cmake(Qt5LinguistTools)
BuildRequires:	pkgconfig(libzstd)


%description
CoolReader 3.X is free open-source (GPL) multiplatform version under active
development.

	
%files -f cr3.lang
%license LICENSE
%{_bindir}/cr3
%{_datadir}/applications/cr3.desktop
%dir %{_datadir}/cr3
%{_datadir}/cr3/*.css
%{_datadir}/cr3/backgrounds/
%{_datadir}/cr3/hyph/
%{_datadir}/cr3/textures/
%{_datadir}/pixmaps/cr3.*
#{_metainfodir}/cr3.appdata.xml
%{_mandir}/man1/cr3.1*
%doc %{_docdir}/cr3
%doc README.md

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

	
%find_lang cr3 --with-qt --without-mo
