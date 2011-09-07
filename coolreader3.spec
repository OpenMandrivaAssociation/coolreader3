%define		shortname	cr3

Name:		coolreader3
Version:	3.0.45
Release:	%mkrel 1
Summary:	Free e-book reader
Group:		Books/Literature
License:	GPL
Source:		%{name}-%{version}.tar.bz2
Patch:		%{name}.desktop.patch
URL:		http://www.coolreader.org
BuildRequires:	libqt4-devel, cmake, libpng-devel, libjpeg-devel, libfontconfig-devel, zlib1-devel

%description
Free e-book reader

%prep
%setup -q
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
%{_bindir}/%{shortname}
%{_datadir}/%{shortname}/*.css
%{_datadir}/%{shortname}/i18n/*.qm
%{_datadir}/%{shortname}/hyph/*.pdb
%{_datadir}/%{shortname}/textures/textures/*.jpg
%{_datadir}/%{shortname}/backgrounds/backgrounds/*.jpg
%{_datadir}/pixmaps/%{shortname}.*
%{_datadir}/applications/%{shortname}.desktop
%{_datadir}/doc/%{shortname}/*
%{_mandir}/man1/%{shortname}.*

%clean
rm -rf %{buildroot}