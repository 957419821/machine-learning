echo "running log: " > log
cd lib
python generate_data.py >> ../log
python regression.py >> ../log
