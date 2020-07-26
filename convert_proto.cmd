SET dir=%~dp0
SET mediapipe_official_home=%1
SET /a cnt=0
echo dir is: %dir%
echo mediapipe_official_home is :%mediapipe_official_home%
cd /d %dir%

xcopy %mediapipe_official_home%\*.proto . /s /y
xcopy %mediapipe_official_home%\mediapipe\graphs\*.pbtxt mediapipe\graphs /s /y

for /R %mediapipe_official_home% %%i in (*.proto) do (
    set /a cnt=cnt+1

    REM echo %%~nxi>>1.txt
    REM echo %%i>>1.txt
    protoc -I=%mediapipe_official_home% --python_out=. %%i
)
echo %cnt%