Summary:	Port of Digital Psychosis' 1994 platform shooter
Summary(pl.UTF-8):	Port gry platformowej napisanej przez Digital Psychosis w 1994 roku
Name:		asylum
Version:	0.2
Release:	0.1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/sdl-asylum/%{name}-%{version}.tar.gz
# Source0-md5:	38ce8d0b2b58748a5499239aa8dfd090
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
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -x c++"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
