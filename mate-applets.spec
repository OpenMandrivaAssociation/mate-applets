%define url_ver %(echo %{version}|cut -d. -f1,2)

Summary:	Small applications which embed themselves in the MATE panel
Name:		mate-applets
Version:	1.8.1
Release:	3
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	xsltproc
BuildRequires:	yelp-tools
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-audio-0.10)
BuildRequires:	pkgconfig(gstreamer-interfaces-0.10)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtksourceview-2.0)
#BuildRequires:	pkgconfig(gucharmap-2)
BuildRequires:	pkgconfig(ice)
BuildRequires:	pkgconfig(libgtop-2.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libmatepanelapplet-4.0)
BuildRequires:	pkgconfig(libwnck-1.0)
BuildRequires:	pkgconfig(mateweather)
BuildRequires:	pkgconfig(mate-desktop-2.0)
BuildRequires:	pkgconfig(mate-icon-theme)
BuildRequires:	pkgconfig(mate-settings-daemon)
BuildRequires:	pkgconfig(NetworkManager)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(pygobject-2.0)
BuildRequires:	pkgconfig(pygtk-2.0)
BuildRequires:	pkgconfig(sm)
BuildRequires:	pkgconfig(upower-glib)

Requires:	dbus
Requires:	mate-panel
Requires:	mate-system-monitor
Requires:	polkit-mate
Requires:	pygtk2.0-libglade
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
%configure \
	--libexecdir=%{_libexecdir}/mate-applets \
	--enable-ipv6 \
	--enable-polkit \
	--enable-suid=no

%make

%install
MATECONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std

# remove unneeded converters
rm -fr %{buildroot}%{_datadir}/MateConf

%find_lang %{name} --with-gnome --all-name

%pre
if [ "$1" = "2" -a -d %{_libdir}/invest-applet ]; then
 /bin/rm -rf %{_libdir}/invest-applet 
fi

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/org.mate.CPUFreqSelector.conf
%config(noreplace) %{_sysconfdir}/sound/events/mate-battstat_applet.soundlist
%{_bindir}/*
%{_libexecdir}/mate-applets/*applet*
%{_datadir}/dbus-1/system-services/org.mate.CPUFreqSelector.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.AccessxStatusAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.BattstatAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.CharpickerAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.CPUFreqAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.CommandAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.DriveMountAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.GeyesAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateWeatherAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.MultiLoadAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.StickyNotesAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.TimerAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.TrashAppletFactory.service
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.battstat.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.charpick.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.geyes.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.multiload.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.stickynotes.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.cpufreq.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.command.gschema.xml
%{_datadir}/glib-2.0/schemas/org.mate.panel.applet.timer.gschema.xml
%{_datadir}/mate-applets/*
%{_datadir}/mate-2.0/ui/*
%{_datadir}/mate-panel/applets/org.mate.applets.AccessxStatusApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.BattstatApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.CharpickerApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.CommandApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.CPUFreqApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.DriveMountApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.GeyesApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.MateWeatherApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.MultiLoadApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.StickyNotesApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.TimerApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.TrashApplet.mate-panel-applet
%{_datadir}/pixmaps/*
%{_datadir}/polkit-1/actions/org.mate.cpufreqselector.policy
%{_iconsdir}/hicolor/*/apps/*
%{_iconsdir}/mate/48x48/apps/ax-applet.png
#{py_sitedir}/mate_invest

