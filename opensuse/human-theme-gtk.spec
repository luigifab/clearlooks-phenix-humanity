Name:          human-theme-gtk
Version:       1.3.0
Release:       0
Summary:       Human theme for GTK
Summary(fr):   Thème Human pour GTK
License:       GPL-3.0-or-later and LGPL-2.1-or-later and CC-BY-SA-3.0
URL:           https://github.com/luigifab/human-theme
Source0:       %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:     noarch
BuildRequires: aspell-fr
Recommends:    gtk2-engine-murrine
Recommends:    gnome-icon-theme
Recommends:    dmz-cursor-themes
# https://software.opensuse.org/search?baseproject=openSUSE%3AFactory&q=qt+theme+gtk
Suggests:      libqt5-qtstyleplugins-platformtheme-gtk2
Suggests:      libqt5-qtbase-platformtheme-gtk3
Suggests:      qt6-platformtheme-gtk3

%description %{expand:
This theme works with: GTK 2.24+ (with gtk2-engine-murrine),
GTK 3.20+ (including 3.22 and 3.24), and GTK 4.0+ (experimental).
It is mainly intended for MATE Desktop Environment.

After installation you must restart your session.}

%description -l fr %{expand:
Ce thème fonctionne avec : GTK 2.24+ (avec gtk2-engine-murrine),
GTK 3.20+ (y compris 3.22 et 3.24), et GTK 4.0+ (expérimental).
Il est principalement destiné pour l'environnement de bureau Mate.

Après l'installation vous devez redémarrer votre session.}


%prep
%setup -q -n human-theme-%{version}
# openSUSE use pango 1.44+
sed -i 's/<border name="title_border" left="2" right="2" top="4" bottom="3"/<border name="title_border" left="2" right="2" top="4" bottom="4"/g' src/human-theme/metacity-1/metacity-theme-1.xml
sed -i 's/padding: 4px 3px; \/\* WARNING/padding: 4px 3px 2px; \/\* WARNING/g' src/human-theme/gtk-3.0/base.css
sed -i 's/padding: 3px; \/\* WARNING/padding: 3px 3px 2px; \/\* WARNING/g' src/human-theme/gtk-3.0/base.css
sed -i 's/margin: -7px -10px -4px; \/\* WARNING/margin: -7px -10px -5px; \/\* WARNING/g' src/human-theme/gtk-3.0/base.css

%build

%install
mkdir -p %{buildroot}/etc/profile.d/
mkdir -p %{buildroot}%{_datadir}/themes/
install -p -m 644 debian/profile.sh %{buildroot}/etc/profile.d/human-theme-gtk.sh
cp -a src/human-theme/        %{buildroot}%{_datadir}/themes/
cp -a src/human-theme-blue/   %{buildroot}%{_datadir}/themes/
cp -a src/human-theme-green/  %{buildroot}%{_datadir}/themes/
cp -a src/human-theme-orange/ %{buildroot}%{_datadir}/themes/

%files
%config(noreplace) /etc/profile.d/human-theme-gtk.sh
%license LICENSE
%doc README.md
# the entire source code is GPL-3.0-or-later, except metacity-1/* which is LGPL-2.1-or-later, and gtk-2.0/* which is CC-BY-SA-3.0+
%{_datadir}/themes/human-theme/
%{_datadir}/themes/human-theme-blue/
%{_datadir}/themes/human-theme-green/
%{_datadir}/themes/human-theme-orange/


%changelog
* Wed May 05 2021 Fabrice Creuzot <code@luigifab.fr> - 1.3.0-1
- New upstream version

* Sun Apr 04 2021 Fabrice Creuzot <code@luigifab.fr> - 1.2.0-1
- Initial openSUSE package release
