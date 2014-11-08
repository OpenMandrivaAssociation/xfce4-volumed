%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A volume keys control daemon for Xfce
Name:		xfce4-volumed
Version:	0.1.13
Release:	4
License:	GPLv3
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/applications/xfce4-volumed/
Source0:	http://archive.xfce.org/src/apps/xfce4-volumed/%{url_ver}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(libxfconf-0)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-audio-0.10)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(keybinder)

%description
This daemon is responsible of making the volume up/down
and mute keys of the keyboard work automatically.

%prep
%setup -q

%build
%configure \
	--with-libnotify
%make

%install
%makeinstall_std

%files
%doc ChangeLog AUTHORS THANKS
%{_sysconfdir}/xdg/autostart/xfce4-volumed.desktop
%{_bindir}/xfce4-volumed
