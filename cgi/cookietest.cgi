#!/usr/bin/perl

use strict;
use CGI qw/:standard :html3/;
use CGI::Cookie;
use CGI::Carp qw(fatalsToBrowser warningsToBrowser);
use Data::Dumper;

my $cgi = new CGI;
my $found = "nope";
my $value = "";
my $cook;
# See if the cookie exists
my %cookies = CGI::Cookie->fetch();
if($cookies{MY_COOKIE}) {
	$found = "YES!!";
	$cook = $cgi->cookie('MY_COOKIE');
}
# Otherwise, create a new cookie and set it
else {
	$cook = $cgi->cookie(-name=>'MY_COOKIE',
						-value=>'data');
}
# Set the cookie in the header
print $cgi->header(-cookie=>$cook),
  start_html(-title=>'Test Page',
			 -STYLE=>('http://www.w3.org/StyleSheets/Core/parser.css?family=1&doc=CGI')
			 );

my $esuccess = 0;

print "Cookie: $found: ", Dumper($cookies{MY_COOKIE});
#print br;
#print "All cookies:<br>";
#for (keys %cookies) {
#	print " - $cookies{$_}<br>";
#}

print
	  h1('Welcome to the BiRG'),
	  h3("<em>(...where you WILL be assimilated)</em>"),p,
      start_form,
      "\nEnter your name: ",textfield('uname'),p,
      "\nEnter your email address: ",textfield('uemail'),p,
	  "\nEnter the subject line: ",textfield('esub'),p,
	  "\nEnter the information you would like to send: ",p,
	  	textarea(-name=>'estr',
						-default=>"Text for Email",
						-rows=>10,
						-columns=>50),p,
	  checkbox(-name=>'send_mail',
	  					-default=>0,
						-label=>"Send Email"),p;
# Create the portion for the DNA stuff...
print 
	  "\nEnter the DNA sequence: ",textfield(-name=>'dna'),p,
	  checkbox(-name=>'dna_w_mail',
	  		   -default=>1,
			   -label=>"Send DNA solutions to email"),p,
	  submit,
      end_form,
      hr,"\n";


print end_html;
