%define		shortname	cr

Name:		coolreader3
Version:	3.0.56
Release:	%mkrel 1
Summary:	Free e-book reader
Group:		Books/Literature
License:	GPL
Source:		%{shortname}3_%{version}.orig.tar.gz
Patch:		%{shortname}3.desktop.patch
URL:		http://www.coolreader.org
BuildRequires:	libqt4-devel, cmake, libpng-devel, libjpeg-devel, zlib1-devel
BuildRequires:	pkgconfig(libfontconfig)

%description
Free e-book reader

%prep
%setup -q -n %{shortname}%{version}-7
%patch -p0

%build
mkdir qtbuild
cd qtbuild
cmake -D GUI=QT -D CMAKE_BUILD_TYPE=Release -D MAX_IMAGE_SCALE_MUL=2 -D DOC_DATA_COMPRESSION_LEVEL=3 -D DOC_BUFFER_SIZE=0x1400000 -D CMAKE_INSTALL_PREFIX=/usr ..
%make

%install
cd qtbuild
%makeinstall_std

%files
%defattr(-,root,root)
%{_bindir}/%{shortname}3
%{_datadir}/%{shortname}3/*.css
%{_datadir}/%{shortname}3/i18n/*.qm
%{_datadir}/%{shortname}3/hyph/*.pdb
%{_datadir}/%{shortname}3/textures/*.jpg
%{_datadir}/%{shortname}3/backgrounds/*.jpg
%{_datadir}/pixmaps/%{shortname}3.*
%{_datadir}/applications/%{shortname}3.desktop
%{_datadir}/doc/%{shortname}3/*
%{_mandir}/man1/%{shortname}3.*

%clean
rm -rf %{buildroot}