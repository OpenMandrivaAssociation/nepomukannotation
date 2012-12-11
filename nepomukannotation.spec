Name:		nepomukannotation
Version:	0.2.0
Release:	4
Summary:	Set of tools that provides annotation suggestions for Nepomuk
Group:		Graphical desktop/KDE
License:	GPLv2+
Url:		http://quickgit.kde.org/?p=%name.git
Source0:	%{name}-%{version}.tar.bz2
Patch0:		nepomukannotation-0.2.0-fix-build.patch
Patch1:		nepomukannotation-0.2.0-soprano.patch
Patch2:		nepomukannotation-0.2.0-linkage.patch
BuildRequires:	doxygen
BuildRequires:	kdelibs4-devel
BuildRequires:	kdebase4-devel
BuildRequires:	kdebase4-workspace-devel
BuildRequires:	tesseract-devel
BuildRequires:	nepomukextras-devel

%description
A library and a set of tools that provide annotation suggestions.

%files -f %{name}.lang
%{_kde_bindir}/nepomuksimpleannotator
%{_kde_bindir}/nepomuktextannotator
%{_kde_bindir}/resourceeditor
%{_kde_libdir}/kde4/*
%{_kde_applicationsdir}/nepomuksimpleannotator.desktop
%{_kde_applicationsdir}/nepomuktextannotator-app.desktop
%{_kde_datadir}/dbus-1/interfaces/org.kde.nepomuk.UserContextService.xml
%{_kde_services}/nepomukannotationplugins/contextannotationplugin.desktop
%{_kde_services}/nepomukannotationplugins/dbpediaannotationplugin.desktop
%{_kde_services}/nepomukannotationplugins/geonamesannotationplugin.desktop
%{_kde_services}/nepomukannotationplugins/nepomuk_tagsannotationplugin.desktop
%{_kde_services}/nepomukannotationplugins/nepomuk_webpageannotationplugin.desktop
%{_kde_services}/nepomukannotationplugins/pimoannotationplugin.desktop
%{_kde_services}/nepomukannotationplugins/pimotypeannotationplugin.desktop
%{_kde_services}/nepomukannotationplugins/propertycreationannotationplugin.desktop
%{_kde_services}/nepomukmenuplugin.desktop
%{_kde_services}/nepomukusercontextservice.desktop
%{_kde_services}/plasma-applet-nepomukcontextchooser.desktop
%{_kde_servicetypes}/nepomuk-annotationplugin.desktop

#-------------------------------------------------------------------------

%define nepomukannotation_major 0
%define libnepomukannotation %mklibname nepomukannotation %{nepomukannotation_major}

%package -n %{libnepomukannotation}
Summary:	%{name} library
Group:		System/Libraries

%description -n %{libnepomukannotation}
A library and a set of tools that provide annotation suggestions. 

%files -n %{libnepomukannotation}
%{_kde_libdir}/libnepomukannotation.so.%{nepomukannotation_major}*

#-------------------------------------------------------------------------

%package devel
Summary:	%{name} devel headers
Group:		System/Libraries
Requires:	%{libnepomukannotation} = %{version}-%{release}

%description devel
A library and a set of tools that provide annotation suggestions.

This package provides the devel files for %{name}

%files devel
%{_kde_includedir}/nepomuk/*
%{_kde_libdir}/libnepomukannotation.so
%{_kde_datadir}/cmake/NepomukAnnotation

#-------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
%global ldflags %{ldflags} -fuse-ld=bfd
%cmake_kde4
%make

%install
%makeinstall_std -C build
%find_lang --all-name nepomukannotation nepomuk_propertycreationannotationplugin nepomuk_pimoannotationplugin nepomuk_geonamesannotationplugin nepomuk_pimotypeannotationplugin nepomuk_webpageannotationplugin plasma_applet_nepomukcontextchooser nepomukmenuplugin %{name}.lang

