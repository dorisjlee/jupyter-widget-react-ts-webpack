npx webpack
pip install .
jupyter nbextension install --sys-prefix --symlink --overwrite --py displayWidget
jupyter nbextension enable --sys-prefix --py displayWidget
