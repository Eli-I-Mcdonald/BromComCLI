cd /opt/bromcom
/usr/local/bin/bromcom-cli > homework.txt
cat homework.txt
shred -xfu page.txt
cd - >/dev/null
