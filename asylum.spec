# TODO:
# - fix install score dir, because game crashes after start

Summary:	Port of Digital Psychosis' 1994 platform shooter
Summary(pl.UTF-8):	Port gry platformowej napisanej przez Digital Psychosis w 1994 roku
Name:		asylum
Version:	0.2.2
Release:	0.1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/sdl-asylum/%{name}-%{version}.tar.gz
# Source0-md5:	e349a99bf099df818b0efc4f83359858
Patch0:		%{name}-makefile.patch
URL:		http://sourceforge.net/projects/sdl-asylum/
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
	CFLAGS="%{rpmcxxflags} -DRESOURCEPATH=\\\"%{_datadir}/asylum\\\" -DSCOREPATH=\\\"/var/games/asylum\\\""

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(2755,root,games) %{_bindir}/%{name}
%{_datadir}/%{name}
%attr(775,root,games) %dir /var/games/asylum
