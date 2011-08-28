Name:		coolreader3
Version:	3.0.45
Release:	%mkrel 1
Summary:	Free e-book reader
Group:		Books/Literature
License:	GPL
Source:		%{name}-%{version}.tar.bz2
URL:		http://www.coolreader.org
BuildRequires:	libqt4-devel, cmake, libpng-devel, libjpeg-devel, libfontconfig-devel, zlib1-devel

%description
Free e-book reader

%prep
%setup -q

%build
mkdir qtbuild
cd qtbuild
cmake -D GUI=QT -D CMAKE_BUILD_TYPE=Release -D MAX_IMAGE_SCALE_MUL=2 -D DOC_DATA_COMPRESSION_LEVEL=3 -D DOC_BUFFER_SIZE=0x1400000 -D CMAKE_INSTALL_PREFIX=/usr ..
%make
#make install



