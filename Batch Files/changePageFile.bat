wmic pagefileset where name="C:\\pagefile.sys" set InitialSize=32,MaximumSize=512

wmic pagefile list /format:list

pause