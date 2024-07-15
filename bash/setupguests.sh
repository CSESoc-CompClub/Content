#!/usr/bin/expect -f
# setupguests - login as guests and run a script

set prompt "\\$ $"

if { $argc < 1 } {
        send_user "Usage: $argv0 script num...\n"
        exit
}

# Shift a list and return the first element. Taken from Tcl Gems.
proc lshift {inputlist} {
	upvar $inputlist argv
	set arg [lindex $argv 0]
	set argv [lreplace $argv[set argv {}] 0 0]
	return $arg
}

# When we call su, we change to the home directory. So resolve a
# relative path to the script.
set script [exec realpath [lshift argv]]

# Read the guest account password. Receiving it as an argument is a
# security risk, because it will appear in the process list. Instead, we
# prompt the user ourselves. Taken from expect(1).
stty -echo
send_user "Password: "
expect_tty -re "(.*)\n"
set password $expect_out(1,string)
send_user "\n"
stty echo

foreach num $argv {
	# Guest account numbers are at least two digits long.
	spawn su --login cseguest[format %02s $num]
	expect Password
	send "$password\r"
	expect {
		failure {close ; break}
		-re $prompt
	}
	send "$script\r"
	# Wait for the shell prompt again before closing.
	expect -re $prompt
	close
}
