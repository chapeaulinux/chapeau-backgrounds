Name:           chapeau-backgrounds
Version:        1.1
Release:        5%{?dist}
Summary:        Backgrounds for Chapeau

Group:          Applications/Multimedia
License:        CC-BY
URL:            http://chapeaulinux.org
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch

%description
A selection of backgrounds for the Chapeau linux distribution

%prep
%setup -c


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/backgrounds/chapeau
for i in wallpapers/*
	do
		install -m0644 $i $RPM_BUILD_ROOT%{_datadir}/backgrounds/chapeau
	done
install -Dm0644 chapeau-backgrounds.xml $RPM_BUILD_ROOT%{_datadir}/gnome-background-properties/chapeau-backgrounds.xml


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%{_datadir}/backgrounds
%{_datadir}/gnome-background-properties

%changelog
* Tue Nov 10 2015 Vince Pooley <vince@chapeaulinux.org> - 1.1-5
- Even more tasty backgrounds
- Tweaked chapeau_misty_blur_branded_wallpaper.jpg

* Tue Nov 03 2015 Vince Pooley <vince@chapeaulinux.org> - 1.1-4
- Additional backgrounds including Chapeau 23's default

* Wed Apr 01 2015 Vince Pooley <vince@chapeaulinux.org> - 1.1-3
- Additional backgrounds including Chapeau 22's default

* Sun Feb 01 2015 Vince Pooley <vince@chapeaulinux.org> - 1.1-2
- Fixed incorrect option & shade type on Chapeau Grassy background.

* Thu Jan 15 2015 Vince Pooley <vince@chapeaulinux.org> - 1.1-1
- Additional backgrounds and amended shade types

* Thu Jan 08 2015 Vince Pooley <vince@chapeaulinux.org> - 1.0-1
- Initial release
