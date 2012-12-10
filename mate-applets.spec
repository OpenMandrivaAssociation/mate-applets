Summary:	Small applications which embed themselves in the MATE panel
Name:		mate-applets
Version:	1.4.0
Release:	2
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
Patch0:		mate-applets-1.2.3_format_not_a_string_literal.patch

BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd43-xml
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	rarian
BuildRequires:	xsltproc
#BuildRequires:	cpufrequtils-devel
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-audio-0.10)
BuildRequires:	pkgconfig(gstreamer-interfaces-0.10)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libmatenotify)
BuildRequires:	pkgconfig(libmatepanelapplet-2.0)
BuildRequires:	pkgconfig(libmatewnck)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(mateweather)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(mate-doc-utils)
BuildRequires:	pkgconfig(mate-icon-theme)
BuildRequires:	pkgconfig(mate-python-2.0)
BuildRequires:	pkgconfig(mate-settings-daemon)
#BuildRequires:	pkgconfig(gucharmap)
BuildRequires:	pkgconfig(NetworkManager)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(upower-glib)
BuildRequires:	python-mate-applet

Requires:	dbus
Requires(pre,preun,post):	mate-conf
Requires:	mate-panel
Requires:	mate-system-monitor
Requires:	polkit-mate
Requires:	pygtk2.0-libglade
Requires:	python-mate-applet
#Requires:	python-mate-extras
Requires:	python-mateconf
Requires:	usermode-consoleonly

%description
MATE (GNU Network Object Model Environment) is a user-friendly
set of applications and desktop tools to be used in conjunction with a
window manager for the X Window System.  MATE is similar in purpose and
scope to CDE and KDE, but MATE (like KDE) is based completely on Open Source
software.  The mate-applets package provides Panel applets which
enhance your MATE experience.

You should install the mate-applets package if you would like to abuse the
MATE desktop environment by embedding small utilities in the MATE panel.

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--libexecdir=%{_libexecdir}/mate-applets \
	--enable-ipv6 \
	--enable-mini-commander \
	--enable-mixer-applet \
	--enable-polkit \
	--enable-suid=no \
	--disable-scrollkeeper \
	--disable-schemas-install

%make

%install
MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std
%find_lang %{name} --with-gnome --all-name

%pre
if [ "$1" = "2" -a -d %{_libdir}/invest-applet ]; then
 /bin/rm -rf %{_libdir}/invest-applet 
fi

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%{_sysconfdir}/dbus-1/system.d/org.mate.CPUFreqSelector.conf
%{_sysconfdir}/mateconf/schemas/charpick.schemas
%{_sysconfdir}/mateconf/schemas/cpufreq-applet.schemas
%{_sysconfdir}/mateconf/schemas/drivemount.schemas
%{_sysconfdir}/mateconf/schemas/geyes.schemas
%{_sysconfdir}/mateconf/schemas/mini-commander-global.schemas
%{_sysconfdir}/mateconf/schemas/mini-commander.schemas
%{_sysconfdir}/mateconf/schemas/mixer.schemas
%{_sysconfdir}/mateconf/schemas/multiload.schemas
%{_sysconfdir}/mateconf/schemas/stickynotes.schemas
%{_sysconfdir}/mateconf/schemas/battstat.schemas
%{_sysconfdir}/sound/events/mate-battstat_applet.soundlist
%{_bindir}/*
%{_libexecdir}/matecomponent/servers/*.server
%{_libexecdir}/mate-applets/*applet*
%{_datadir}/dbus-1/system-services/org.mate.CPUFreqSelector.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.AccessxStatusAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.BattstatAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.CPUFreqAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.CharpickerAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.DriveMountAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.GeyesAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateWeatherAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.MiniCommanderAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.MixerAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.MultiLoadAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.StickyNotesAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.TrashAppletFactory.service
%{_datadir}/mate-applets/*
%{_datadir}/mate-2.0/ui/*
%{_datadir}/mate-panel/applets/org.mate.applets.AccessxStatusApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.BattstatApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.CPUFreqApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.CharpickerApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.DriveMountApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.GeyesApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.MateWeatherApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.MiniCommanderApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.MixerApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.MultiLoadApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.StickyNotesApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.TrashApplet.mate-panel-applet
%{_datadir}/pixmaps/*
%{_datadir}/polkit-1/actions/org.mate.cpufreqselector.policy
%{_iconsdir}/hicolor/*/apps/*
%{_iconsdir}/mate/48x48/apps/ax-applet.png
%{py_sitedir}/mate_invest



%changelog
* Mon Jun 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.3-3
+ Revision: 804620
- rebuild to move applets to libexecdir/mate-applets

* Fri Jun 08 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.3-2
+ Revision: 803297
- rebuild for correct reqs

* Tue Jun 05 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.3-1
+ Revision: 802797
- imported package mate-applets

