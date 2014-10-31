#!/usr/bin/perl

use strict;
use Fcntl qw(:flock); # import LOCK_*
use CGI;

my $cgi = CGI->new();

# Start the page by outputing the Content-type header
print $cgi->header;
print $cgi->start_html("Locking a file for reading");

# Read the file and find the number
open my $LOCKFILE, "<", "lockfile"
       or die "Unable to open lockfile: $!\n";
my $err = flock $LOCKFILE, LOCK_EX;
my $number = <$LOCKFILE>;
close $LOCKFILE;

$number++;

# Write the new number to the lockfile
open my $LOCKFILE, ">", "lockfile";
print $LOCKFILE "$number\n";

# Sleep for a random amount of time
my $rand_sleep = rand(5);
print "My random sleeping time is $rand_sleep seconds<br>";
sleep(rand(10));
close $LOCKFILE;

flock $LOCKFILE, LOCK_UN;

print $cgi->h3("My value is $number");
print $cgi->end_html();
