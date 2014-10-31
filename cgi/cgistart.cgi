#!/usr/bin/perl

use CGI;

$cgi = CGI->new();

# Start the page by outputing the Content-type header
print $cgi->header;
print $cgi->start_html("Using the CGI class");

print "<h1>This is a list of the environment variables</h1>\n";
print $cgi->hr();

print "<pre>\n";

foreach $var (sort(keys(%ENV))) {
    $val = $ENV{$var};
    $val =~ s|\n|\\n|g;
    $val =~ s|"|\\"|g;
    print "${var}=\"${val}\"\n";
}

print "</pre>\n";

print $cgi->hr();

$reqmeth = $cgi->request_method();

####################################################
# Decide if GET or POST
####################################################
if ($reqmeth eq "POST")
{
    print $cgi->h2("This is a POST");
    print "The Query String is empty. The arguments\n";
    print "come in the body of the HTTP request\n";
    print " message. Here it is.\n";
}
elsif ($reqmeth eq "GET")
{
    print $cgi->h2("This is a GET");
    print "The Query String is in the environment\n";
}
else
{
    print "<h2>Unknown method</h2>\n";
}

print "<pre>\n";

@names = $cgi->param;
$i = 0;
foreach $n (@names)
{
    print "Arg $i name is: [$n]\n";
    $value = $cgi->param($n);
    print "Arg $i value is: [$value]\n";
    $i++;
}

print "</pre>\n";
print "<h2>All done now... bye</h2>\n";
print $cgi->end_html();
