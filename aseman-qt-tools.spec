%global channel stable

%if 0%{?fedora} <= 24
%global _qt5_qmldir %{_qt5_archdatadir}/qml
%endif

Name:           aseman-qt-tools
Version:        1.0.0
Release:        1%{?dist}
Summary:        Shared tools and functions, used in the aseman's projects

License:        GPLv3+
URL:            https://github.com/Aseman-Land/%{name}
Source0:        %{url}/archive/v%{version}-%{channel}/%{name}-%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtquick1-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsensors-devel
BuildRequires:  qt5-qtlocation-devel
BuildRequires:  qtkeychain-qt5-devel

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}-%{channel}
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
* Sat Jul 23 2016 Igor Gnatenko <ignatenko@redhat.com> - 1.0.0-1
- Initial package
