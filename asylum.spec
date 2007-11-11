Summary:	Port of Digital Psychosis' 1994 platform shooter
Summary(pl.UTF-8):	Port gry platformowej napisanej przez Digital Psychosis w 1994 roku
Name:		asylum
Version:	0.2.3
Release:	0.1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/sdl-asylum/%{name}-%{version}.tar.gz
# Source0-md5:	ae381080926d3837235cc3c2eaf081f1
Patch0:		%{name}-makefile.patch
URL:		http://sdl-asylum.sourceforge.net/
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A port of Digital Psychosis' 1994 platform shooter for the Acorn
Archimedes.

%description -l pl.UTF-8
Port napisaj przez Digital Psychosis w 1994 roku strzelaniny
platformowej dla komputera Acorn Archimedes.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cxx}" \
	OPTFLAGS="%{rpmcxxflags} -DRESOURCEPATH=\\\"%{_datadir}/asylum\\\" -DSCOREPATH=\\\"/var/games/asylum\\\""

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Instruct README
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/%{name}
%attr(775,root,games) %dir /var/games/asylum
