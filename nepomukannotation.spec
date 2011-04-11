Name:          nepomukannotation
Version:       0.2.0
Release:       %mkrel 1
Summary:       Nepomuk support files
Group:         Graphical desktop/KDE
License:       GPLv2+
Url:           http://quickgit.kde.org/?p=kolena.git
Source0:       %{name}-%{version}.tar.bz2
Patch0:        nepomukannotation-0.2.0-fix-build.patch
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: kdelibs4-devel
BuildRequires: tesseract-devel
BuildRequires: nepomukextras-devel

%description
Nepomuk support files

%files -f %name.lang
%defattr(-,root,root)
%_kde_bindir/nepomuksimpleannotator
%_kde_bindir/nepomuktextannotator
%_kde_bindir/resourceeditor
%_kde_libdir/kde4/*
%_kde_datadir/applications/kde4/nepomuksimpleannotator.desktop
%_kde_datadir/applications/kde4/nepomuktextannotator-app.desktop
%_kde_datadir/dbus-1/interfaces/org.kde.nepomuk.UserContextService.xml
%_kde_datadir/kde4/services/nepomukannotationplugins/contextannotationplugin.desktop
%_kde_datadir/kde4/services/nepomukannotationplugins/dbpediaannotationplugin.desktop
%_kde_datadir/kde4/services/nepomukannotationplugins/geonamesannotationplugin.desktop
%_kde_datadir/kde4/services/nepomukannotationplugins/nepomuk_tagsannotationplugin.desktop
%_kde_datadir/kde4/services/nepomukannotationplugins/nepomuk_webpageannotationplugin.desktop
%_kde_datadir/kde4/services/nepomukannotationplugins/pimoannotationplugin.desktop
%_kde_datadir/kde4/services/nepomukannotationplugins/pimotypeannotationplugin.desktop
%_kde_datadir/kde4/services/nepomukannotationplugins/propertycreationannotationplugin.desktop
%_kde_datadir/kde4/services/nepomukmenuplugin.desktop
%_kde_datadir/kde4/services/nepomukusercontextservice.desktop
%_kde_datadir/kde4/services/plasma-applet-nepomukcontextchooser.desktop
%_kde_datadir/kde4/servicetypes/nepomuk-annotationplugin.desktop

#-------------------------------------------------------------------------

%define nepomukannotation_major 0
%define libnepomukannotation %mklibname nepomukannotation %nepomukannotation_major

%package -n %libnepomukannotation
Summary:    Ktorrent libbrary
Group:      System/Libraries

%description -n %libnepomukannotation
KTorrent library.

%files -n %libnepomukannotation
%defattr(-,root,root)
%_kde_libdir/libnepomukannotation.so.%{nepomukannotation_major}*

#-------------------------------------------------------------------------

%package devel
Summary: Ktorrent plugin devel headers
Group: Networking/File transfer
Requires: %{libnepomukannotation} = %{version}

%description devel
Ktorrent plugin devel headers.

%files devel
%defattr(-,root,root)
%_kde_includedir/nepomuk/*
%_kde_libdir/libnepomukannotation.so
%_kde_datadir/cmake/NepomukAnnotation

#-------------------------------------------------------------------------

%prep
%setup -q -n %name-%version
%patch0 -p0

%build
%cmake_kde4 
%make
 
%install
rm -rf %buildroot
%makeinstall_std -C build
%find_lang --all-name nepomukannotation nepomuk_pimoannotationplugin nepomuk_geonamesannotationplugin nepomuk_pimotypeannotationplugin nepomuk_webpageannotationplugin plasma_applet_nepomukcontextchooser nepomukmenuplugin 


%clean
rm -rf %buildroot
