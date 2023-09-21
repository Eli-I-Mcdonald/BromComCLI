#!/bin/sh
executable_name="bromcom-cli"
executable_name2="bromcom"
install_directory="/usr/local/bin"
data_directory="/opt/bromcom"
if [ -n "$1" ]
then executable_name="$1"
fi
test -e ${install_directory}/${executable_name}&& \
read -p "Do you want to replace the already installed version? [Y/n] " input

#if [ "${input}" = "y" ||  "${input}" = "Y" ]
if [ "${input}" = "y" ] || [ "${input}" = "Y" ] || [ "${input}" = "" ]
  then install bromcom-cli.py ${install_directory}/${executable_name}
  echo "${executable_name} installed at ${install_directory}"
  install runner.sh ${install_directory}/${executable_name2}
  echo "${executable_name2} installed at ${install_directory}"
  mkdir ${data_directory} 2>/dev/null
  echo "made directory ${data_directory}"
  chown -R user /opt/bromcom
fi
