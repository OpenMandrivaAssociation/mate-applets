Summary:	Small applications which embed themselves in the MATE panel
Name:		mate-applets
Version:	1.2.3
Release:	3
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-dtd43-xml
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	rarian
BuildRequires:	xsltproc
BuildRequires:	cpufrequtils-devel
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
BuildRequires:	pkgconfig(libwnck-1.0)
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
%{_sysconfdir}/mateconf/schemas/multiload.schemas
%{_sysconfdir}/mateconf/schemas/stickynotes.schemas
%{_sysconfdir}/mateconf/schemas/battstat.schemas
%{_sysconfdir}/sound/events/mate-battstat_applet.soundlist
%{_bindir}/*
%{_libexecdir}/matecomponent/servers/MATE_CDPlayerApplet.server
%{_libexecdir}/matecomponent/servers/MATE_KeyboardApplet.server
%{_libexecdir}/matecomponent/servers/MATE_MailcheckApplet_Factory.server
%{_libexecdir}/matecomponent/servers/MATE_MiniCommanderApplet.server
%{_libexecdir}/matecomponent/servers/MATE_MixerApplet.server
%{_libexecdir}/matecomponent/servers/MATE_NullApplet_Factory.server
%{_libexecdir}/matecomponent/servers/MATE_Panel_WirelessApplet.server
%{_libexecdir}/*applet*
#{py_puresitedir}/invest*
%{_datadir}/dbus-1/system-services/org.mate.CPUFreqSelector.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.AccessxStatusAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.BattstatAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.CPUFreqAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.CharpickerAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.DriveMountAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.GeyesAppletFactory.service
%{_datadir}/dbus-1/services/org.mate.panel.applet.MateWeatherAppletFactory.service
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
%{_datadir}/mate-panel/applets/org.mate.applets.MultiLoadApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.StickyNotesApplet.mate-panel-applet
%{_datadir}/mate-panel/applets/org.mate.applets.TrashApplet.mate-panel-applet
%{_datadir}/pixmaps/*
%{_datadir}/polkit-1/actions/org.mate.cpufreqselector.policy
%{_iconsdir}/hicolor/*/apps/*
%{_iconsdir}/mate/48x48/apps/ax-applet.png
# mate help files
%{_datadir}/mate/help

