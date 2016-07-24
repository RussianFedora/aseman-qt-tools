%global channel stable

# Since Qt 5.7.0 is not needed
%{!?_qt5_qmldir:%global _qt5_qmldir %{_qt5_archdatadir}/qml}

Name:           aseman-qt-tools
Version:        1.0.0
Release:        4%{?dist}
Summary:        Shared tools and functions, used in the aseman's projects

License:        GPLv3+
URL:            https://github.com/Aseman-Land/%{name}
Source0:        %{url}/archive/v%{version}-%{channel}/%{name}-%{version}.tar.gz

# https://github.com/Aseman-Land/aseman-qt-tools/commit/47412ddb26acf227ee6cb6950f6e9ded01f3375c
Patch0001:      0001-add-plugin-definition-in-qmldir.patch

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsensors-devel
BuildRequires:  qt5-qtlocation-devel
BuildRequires:  qtkeychain-qt5-devel

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}-%{channel} -p1
# https://github.com/Aseman-Land/aseman-qt-tools/pull/3
find -type f -executable -exec chmod -x {} ';'
mkdir %{_target_platform}

%build
pushd %{_target_platform}
  %qmake_qt5 ..       \
      QT+=widgets     \
      QT+=multimedia  \
      QT+=dbus        \
      QT+=sensors     \
      QT+=positioning \
      %{nil}
popd
%make_build -C %{_target_platform}

%install
%make_install INSTALL_ROOT=%{buildroot} -C %{_target_platform}

%files
%license LICENSE
%{_qt5_qmldir}/AsemanTools/

%changelog
* Sun Jul 24 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-4
- Replace BR with proper qt5-qtdeclarative

* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-3
- Remove executable flag from files

* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-2
- Backport critical patch

* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-1
- Initial package
