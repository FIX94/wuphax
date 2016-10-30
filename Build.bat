@echo off

mkdir data 2>/nul
cd app_booter
echo.
echo Building App Booter
echo.
make clean
make
mv app_booter.bin ../data

cd ..
echo.
echo Building Loader
echo.
make clean
make

echo.
pause
