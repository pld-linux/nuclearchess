Summary:	An explosive chess variant
Summary(pl):	Wybuchowy wariant szachów
Name:		nuclearchess
Version:	0.9.2
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://user.cs.tu-berlin.de/~karlb/nuclearchess/%{name}-%{version}.tar.gz
# Source0-md5:	10d8b2a2890d6aaca1afe2cbc23f002a
URL:		http://www.linux-games.com/nuclearchess
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NuclearChess is a chess variant. Whenever a piece is captured, both
pieces and all pieces on neighbour fields die.

%description -l pl
NuclearChess jest wariantem szachów. Gdy figura zostaje pojmana, obie
figury wraz ze wszystkimi figurami na s±siednich polach gin±.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
