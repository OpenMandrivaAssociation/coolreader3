%define		shortname	cr

Name:		coolreader3
Version:	3.0.56
Release:	2
Summary:	Free e-book reader
Group:		Books/Literature
License:	GPL
Source0:	%{shortname}3_%{version}.orig.tar.gz
URL:		http://www.coolreader.org
BuildRequires:	pkgconfig(Qt3Support), cmake, libpng-devel, jpeg-devel, zlib1-devel
BuildRequires:	pkgconfig(fontconfig)

%description
CoolReader 3.X is free open-source (GPL) multiplatform version under active
development.

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
cd build
%makeinstall_std

%files
%defattr(-,root,root)
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


%changelog
* Wed Apr 04 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 3.0.56-1mdv2011.0
+ Revision: 789189
- fix BR
- specfile cleanup

  + Sergey Zhemoitel <serg@mandriva.org>
    - update to 3.0.56
    - add new version 3.0.50

* Thu Sep 08 2011 Sergey Zhemoitel <serg@mandriva.org> 3.0.49-1
+ Revision: 698983
- new version 3.0.49
- fix build, add russian comment in .desktop
- fix install in spec

* Sun Aug 28 2011 Sergey Zhemoitel <serg@mandriva.org> 3.0.45-1
+ Revision: 697261
- imported package coolreader3

