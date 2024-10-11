#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : kirigami
Version  : 6.7.0
Release  : 16
URL      : https://download.kde.org/stable/frameworks/6.7/kirigami-6.7.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.7/kirigami-6.7.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.7/kirigami-6.7.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 FSFAP GPL-2.0 LGPL-2.0 LGPL-2.1 LGPL-3.0 MIT
Requires: kirigami-data = %{version}-%{release}
Requires: kirigami-lib = %{version}-%{release}
Requires: kirigami-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : cmake
BuildRequires : extra-cmake-modules-data
BuildRequires : git
BuildRequires : gnupg
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Add here, with either a script that does a git checkout
or as git submodules the two projects:

%package data
Summary: data components for the kirigami package.
Group: Data

%description data
data components for the kirigami package.


%package dev
Summary: dev components for the kirigami package.
Group: Development
Requires: kirigami-lib = %{version}-%{release}
Requires: kirigami-data = %{version}-%{release}
Provides: kirigami-devel = %{version}-%{release}
Requires: kirigami = %{version}-%{release}

%description dev
dev components for the kirigami package.


%package lib
Summary: lib components for the kirigami package.
Group: Libraries
Requires: kirigami-data = %{version}-%{release}
Requires: kirigami-license = %{version}-%{release}

%description lib
lib components for the kirigami package.


%package license
Summary: license components for the kirigami package.
Group: Default

%description license
license components for the kirigami package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n kirigami-6.7.0
cd %{_builddir}/kirigami-6.7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728688108
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1728688108
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/kirigami
cp %{_builddir}/kirigami-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/kirigami/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee || :
cp %{_builddir}/kirigami-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kirigami/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kirigami-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kirigami/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kirigami-%{version}/LICENSES/FSFAP.txt %{buildroot}/usr/share/package-licenses/kirigami/da20b47077b3106fb65720d6fef309f39043fa60 || :
cp %{_builddir}/kirigami-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kirigami/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/kirigami-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kirigami/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/kirigami-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/kirigami/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/kirigami-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/kirigami/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/kirigami-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/kirigami/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/kirigami-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kirigami/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kirigami-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/kirigami/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/kirigami-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/kirigami/81e12d0c07782abcf558af7aa19846e3e2606a70 || :
cp %{_builddir}/kirigami-%{version}/templates/kirigami6/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/kirigami/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/kirigami-%{version}/templates/kirigami6/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/kirigami/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/kirigami-%{version}/templates/kirigami6/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/kirigami/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kdevappwizard/templates/kirigami6.tar.bz2
/usr/share/locale/ar/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/ast/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/az/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/bg/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/ca/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/ca@valencia/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/cs/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/da/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/de/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/el/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/en_GB/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/eo/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/es/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/et/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/eu/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/fi/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/fr/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/gl/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/he/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/hi/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/hu/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/ia/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/id/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/is/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/it/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/ja/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/ka/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/ko/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/lt/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/lv/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/ml/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/nl/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/nn/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/pa/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/pl/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/pt/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/pt_BR/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/ro/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/ru/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/sk/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/sl/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/sr/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/sr@ijekavian/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/sr@ijekavianlatin/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/sr@latin/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/sv/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/ta/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/tg/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/tr/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/uk/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/zh_CN/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/locale/zh_TW/LC_MESSAGES/libkirigami6_qt.qm
/usr/share/qlogging-categories6/kirigami.categories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/Kirigami/Platform/PlatformPluginFactory
/usr/include/KF6/Kirigami/Platform/PlatformTheme
/usr/include/KF6/Kirigami/Platform/StyleSelector
/usr/include/KF6/Kirigami/Platform/TabletModeWatcher
/usr/include/KF6/Kirigami/Platform/Units
/usr/include/KF6/Kirigami/Platform/VirtualKeyboardWatcher
/usr/include/KF6/Kirigami/Platform/kirigamiplatform_export.h
/usr/include/KF6/Kirigami/Platform/kirigamiplatform_version.h
/usr/include/KF6/Kirigami/Platform/platformpluginfactory.h
/usr/include/KF6/Kirigami/Platform/platformtheme.h
/usr/include/KF6/Kirigami/Platform/styleselector.h
/usr/include/KF6/Kirigami/Platform/tabletmodewatcher.h
/usr/include/KF6/Kirigami/Platform/units.h
/usr/include/KF6/Kirigami/Platform/virtualkeyboardwatcher.h
/usr/lib64/cmake/KF6Kirigami/KF6KirigamiConfig.cmake
/usr/lib64/cmake/KF6Kirigami/KF6KirigamiConfigVersion.cmake
/usr/lib64/cmake/KF6Kirigami/KF6KirigamiMacros.cmake
/usr/lib64/cmake/KF6Kirigami/KF6KirigamiTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Kirigami/KF6KirigamiTargets.cmake
/usr/lib64/cmake/KF6Kirigami2/KF6Kirigami2Config.cmake
/usr/lib64/cmake/KF6Kirigami2/KF6Kirigami2ConfigVersion.cmake
/usr/lib64/cmake/KF6KirigamiPlatform/KF6KirigamiPlatformConfig.cmake
/usr/lib64/cmake/KF6KirigamiPlatform/KF6KirigamiPlatformConfigVersion.cmake
/usr/lib64/cmake/KF6KirigamiPlatform/KF6KirigamiPlatformTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6KirigamiPlatform/KF6KirigamiPlatformTargets.cmake
/usr/lib64/libKirigami.so
/usr/lib64/libKirigamiDelegates.so
/usr/lib64/libKirigamiDialogs.so
/usr/lib64/libKirigamiLayouts.so
/usr/lib64/libKirigamiPlatform.so
/usr/lib64/libKirigamiPrimitives.so
/usr/lib64/libKirigamiPrivate.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKirigami.so.6
/usr/lib64/libKirigami.so.6.7.0
/usr/lib64/libKirigamiDelegates.so.6
/usr/lib64/libKirigamiDelegates.so.6.7.0
/usr/lib64/libKirigamiDialogs.so.6
/usr/lib64/libKirigamiDialogs.so.6.7.0
/usr/lib64/libKirigamiLayouts.so.6
/usr/lib64/libKirigamiLayouts.so.6.7.0
/usr/lib64/libKirigamiPlatform.so.6
/usr/lib64/libKirigamiPlatform.so.6.7.0
/usr/lib64/libKirigamiPrimitives.so.6
/usr/lib64/libKirigamiPrimitives.so.6.7.0
/usr/lib64/libKirigamiPrivate.so.6
/usr/lib64/libKirigamiPrivate.so.6.7.0
/usr/lib64/qt6/qml/org/kde/kirigami/AboutItem.qml
/usr/lib64/qt6/qml/org/kde/kirigami/AboutPage.qml
/usr/lib64/qt6/qml/org/kde/kirigami/AbstractApplicationHeader.qml
/usr/lib64/qt6/qml/org/kde/kirigami/AbstractApplicationItem.qml
/usr/lib64/qt6/qml/org/kde/kirigami/AbstractApplicationWindow.qml
/usr/lib64/qt6/qml/org/kde/kirigami/AbstractCard.qml
/usr/lib64/qt6/qml/org/kde/kirigami/Action.qml
/usr/lib64/qt6/qml/org/kde/kirigami/ActionTextField.qml
/usr/lib64/qt6/qml/org/kde/kirigami/ActionToolBar.qml
/usr/lib64/qt6/qml/org/kde/kirigami/ApplicationItem.qml
/usr/lib64/qt6/qml/org/kde/kirigami/ApplicationWindow.qml
/usr/lib64/qt6/qml/org/kde/kirigami/Card.qml
/usr/lib64/qt6/qml/org/kde/kirigami/CardsLayout.qml
/usr/lib64/qt6/qml/org/kde/kirigami/CardsListView.qml
/usr/lib64/qt6/qml/org/kde/kirigami/Chip.qml
/usr/lib64/qt6/qml/org/kde/kirigami/ContextDrawer.qml
/usr/lib64/qt6/qml/org/kde/kirigami/ContextualHelpButton.qml
/usr/lib64/qt6/qml/org/kde/kirigami/FlexColumn.qml
/usr/lib64/qt6/qml/org/kde/kirigami/GlobalDrawer.qml
/usr/lib64/qt6/qml/org/kde/kirigami/Heading.qml
/usr/lib64/qt6/qml/org/kde/kirigami/InlineMessage.qml
/usr/lib64/qt6/qml/org/kde/kirigami/InlineViewHeader.qml
/usr/lib64/qt6/qml/org/kde/kirigami/Kirigami.qmltypes
/usr/lib64/qt6/qml/org/kde/kirigami/LinkButton.qml
/usr/lib64/qt6/qml/org/kde/kirigami/ListItemDragHandle.qml
/usr/lib64/qt6/qml/org/kde/kirigami/ListSectionHeader.qml
/usr/lib64/qt6/qml/org/kde/kirigami/LoadingPlaceholder.qml
/usr/lib64/qt6/qml/org/kde/kirigami/NavigationTabBar.qml
/usr/lib64/qt6/qml/org/kde/kirigami/NavigationTabButton.qml
/usr/lib64/qt6/qml/org/kde/kirigami/OverlayDrawer.qml
/usr/lib64/qt6/qml/org/kde/kirigami/OverlaySheet.qml
/usr/lib64/qt6/qml/org/kde/kirigami/Page.qml
/usr/lib64/qt6/qml/org/kde/kirigami/PagePoolAction.qml
/usr/lib64/qt6/qml/org/kde/kirigami/PageRow.qml
/usr/lib64/qt6/qml/org/kde/kirigami/PasswordField.qml
/usr/lib64/qt6/qml/org/kde/kirigami/PlaceholderMessage.qml
/usr/lib64/qt6/qml/org/kde/kirigami/ScrollablePage.qml
/usr/lib64/qt6/qml/org/kde/kirigami/SearchField.qml
/usr/lib64/qt6/qml/org/kde/kirigami/SelectableLabel.qml
/usr/lib64/qt6/qml/org/kde/kirigami/SwipeListItem.qml
/usr/lib64/qt6/qml/org/kde/kirigami/UrlButton.qml
/usr/lib64/qt6/qml/org/kde/kirigami/delegates/CheckSubtitleDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigami/delegates/IconTitleSubtitle.qml
/usr/lib64/qt6/qml/org/kde/kirigami/delegates/KirigamiDelegates.qmltypes
/usr/lib64/qt6/qml/org/kde/kirigami/delegates/RadioSubtitleDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigami/delegates/SubtitleDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigami/delegates/SwitchSubtitleDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigami/delegates/TitleSubtitle.qml
/usr/lib64/qt6/qml/org/kde/kirigami/delegates/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigami/delegates/libKirigamiDelegatesplugin.so
/usr/lib64/qt6/qml/org/kde/kirigami/delegates/qmldir
/usr/lib64/qt6/qml/org/kde/kirigami/dialogs/Dialog.qml
/usr/lib64/qt6/qml/org/kde/kirigami/dialogs/KirigamiDialogs.qmltypes
/usr/lib64/qt6/qml/org/kde/kirigami/dialogs/MenuDialog.qml
/usr/lib64/qt6/qml/org/kde/kirigami/dialogs/PromptDialog.qml
/usr/lib64/qt6/qml/org/kde/kirigami/dialogs/SearchDialog.qml
/usr/lib64/qt6/qml/org/kde/kirigami/dialogs/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigami/dialogs/libKirigamiDialogsplugin.so
/usr/lib64/qt6/qml/org/kde/kirigami/dialogs/qmldir
/usr/lib64/qt6/qml/org/kde/kirigami/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigami/layouts/FormLayout.qml
/usr/lib64/qt6/qml/org/kde/kirigami/layouts/KirigamiLayouts.qmltypes
/usr/lib64/qt6/qml/org/kde/kirigami/layouts/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigami/layouts/libKirigamiLayoutsplugin.so
/usr/lib64/qt6/qml/org/kde/kirigami/layouts/qmldir
/usr/lib64/qt6/qml/org/kde/kirigami/libKirigamiplugin.so
/usr/lib64/qt6/qml/org/kde/kirigami/platform/KirigamiPlatform.qmltypes
/usr/lib64/qt6/qml/org/kde/kirigami/platform/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigami/platform/libKirigamiPlatformplugin.so
/usr/lib64/qt6/qml/org/kde/kirigami/platform/qmldir
/usr/lib64/qt6/qml/org/kde/kirigami/primitives/KirigamiPrimitives.qmltypes
/usr/lib64/qt6/qml/org/kde/kirigami/primitives/Separator.qml
/usr/lib64/qt6/qml/org/kde/kirigami/primitives/ShadowedImage.qml
/usr/lib64/qt6/qml/org/kde/kirigami/primitives/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigami/primitives/libKirigamiPrimitivesplugin.so
/usr/lib64/qt6/qml/org/kde/kirigami/primitives/qmldir
/usr/lib64/qt6/qml/org/kde/kirigami/private/ActionIconGroup.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/ActionMenuItem.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/ActionsMenu.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/BannerImage.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/ContextDrawerActionItem.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/DefaultCardBackground.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/DefaultChipBackground.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/DefaultPageTitleDelegate.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/EdgeShadow.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/GlobalDrawerActionItem.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/KirigamiPrivate.qmltypes
/usr/lib64/qt6/qml/org/kde/kirigami/private/MobileDialogLayer.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/PrivateActionToolButton.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/PullDownIndicator.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/SwipeItemEventFilter.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/globaltoolbar/AbstractPageHeader.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/globaltoolbar/BreadcrumbControl.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/globaltoolbar/PageRowGlobalToolBarStyleGroup.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/globaltoolbar/PageRowGlobalToolBarUI.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/globaltoolbar/TitlesPageHeader.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/globaltoolbar/ToolBarPageFooter.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/globaltoolbar/ToolBarPageHeader.qml
/usr/lib64/qt6/qml/org/kde/kirigami/private/kde-qmlmodule.version
/usr/lib64/qt6/qml/org/kde/kirigami/private/libKirigamiPrivateplugin.so
/usr/lib64/qt6/qml/org/kde/kirigami/private/qmldir
/usr/lib64/qt6/qml/org/kde/kirigami/qmldir
/usr/lib64/qt6/qml/org/kde/kirigami/styles/Material/InlineMessage.qml
/usr/lib64/qt6/qml/org/kde/kirigami/styles/Material/Theme.qml
/usr/lib64/qt6/qml/org/kde/kirigami/styles/org.kde.desktop/AbstractApplicationHeader.qml
/usr/lib64/qt6/qml/org/kde/kirigami/styles/org.kde.desktop/Theme.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/AbstractApplicationHeader.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/AbstractCard.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/Chip.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/InlineMessage.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/OverlayDrawer.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/OverlaySheet.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/SingletonHeaderSizeGroup.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/private/BackButton.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/private/BorderPropertiesGroup.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/private/ContextIcon.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/private/DrawerHandle.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/private/ForwardButton.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/private/GenericDrawerIcon.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/private/IconPropertiesGroup.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/private/MenuIcon.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/private/PassiveNotificationsManager.qml
/usr/lib64/qt6/qml/org/kde/kirigami/templates/private/qmldir
/usr/lib64/qt6/qml/org/kde/kirigami/templates/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/kirigami/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/kirigami/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/kirigami/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/kirigami/52039e5c19c950d4c7d6ec5da42ebba2c6def7ee
/usr/share/package-licenses/kirigami/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/kirigami/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/kirigami/81e12d0c07782abcf558af7aa19846e3e2606a70
/usr/share/package-licenses/kirigami/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/kirigami/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/kirigami/da20b47077b3106fb65720d6fef309f39043fa60
/usr/share/package-licenses/kirigami/e458941548e0864907e654fa2e192844ae90fc32
