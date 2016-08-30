#!/usr/bin/env bash
zenity --question --timeout 5 --height 10 --title "Your system will be shutdown!" --text "Do you want to continue?" --ok-label "Yes" --cancel-label "No" 
if [[ $? -eq 0 ]]; then
	sudo shutdown now
fi
