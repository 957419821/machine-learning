models=($(ls | grep "^model"))
echo "models log:" > log.txt
for model in ${models[@]}
do
	echo "------------------------------" >> log.txt
	python $model >> log.txt
done
