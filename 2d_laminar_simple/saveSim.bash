#!/bin/sh
cd ${0%/*} || exit 1    # Run from this directory


Re="1200"

mkdir "solution"
new_path="solution/"${Re}
mkdir ${new_path}

cp -R "postProcessing/." ${new_path}
cp -R "VTK" ${new_path}
cp "plots.ipynb" ${new_path}"/plots.ipynb"