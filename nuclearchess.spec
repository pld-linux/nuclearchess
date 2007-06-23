Summary:	An explosive chess variant
Summary(pl.UTF-8):	Wybuchowy wariant szachów
Name:		nuclearchess
Version:	1.0.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://user.cs.tu-berlin.de/~karlb/nuclearchess/%{name}-%{version}.tar.gz
# Source0-md5:	c36b0cec8ff1bf3525a12aaf8a9c53fe
URL:		http://www.linux-games.com/nuclearchess/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	SDL_image-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NuclearChess is a chess variant. Whenever a piece is captured, both
pieces and all pieces on neighbour fields die.

%description -l pl.UTF-8
NuclearChess jest wariantem szachów. Gdy figura zostaje pojmana, obie
figury wraz ze wszystkimi figurami na sąsiednich polach giną.

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
