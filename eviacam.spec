Name:		eviacam
Version:	1.5.3
Release:	%mkrel 1
Summary:	A Cross-Platform Webcam Based Mouse Emulator
License:	GPLv3+
Group:		Accessibility
URL:		https://eviacam.sourceforge.net/eviacam.php
Source:		%{name}-%{version}.tar
BuildRequires:	wxgtku-devel
BuildRequires:	opencv-devel
BuildRequires:	libxtst-devel
BuildRequires:	libdc1394-devel
BuildRequires:	pkgconfig(libv4l2)
BuildRequires:	gettext-devel
BuildRequires:	dos2unix

%description
Enable Viacam (aka eViacam) is a mouse replacement software that moves
the pointer as you move your head. It works on standard PCs equipped 
with a web camera. No additional hardware is required. Based on the 
award winning Facial Mouse software.

%prep
%setup -q

#Clean up spurious-executable-perm and end-of-line-encoding
%__chmod 0644 COPYING AUTHORS ChangeLog COPYING README THANKS TODO
dos2unix COPYING AUTHORS ChangeLog COPYING README THANKS TODO


%build
./autogen.sh
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

# Remove ast language file
%__rm -rf %{buildroot}%{_datadir}/locale/ast

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING README THANKS TODO
%{_bindir}/%{name}
%{_bindir}/eviacamloader
%{_datadir}/%{name}
%{_datadir}/pixmaps/*.xpm
%{_datadir}/applications/%{name}.desktop

