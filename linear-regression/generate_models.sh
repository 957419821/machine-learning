# Author Liushuai tomeasure@foxmail.com

i=0
while [ $i -lt 10 ]
do
	model="model$(($i+1)).py"
	echo "import linear_regression as lr" > $model
	w_b_tuple="($(($RANDOM%10)), $(($RANDOM%10)))"
	echo "print(\"-----------------------------------\")" >> $model
	echo "print(\"$model: \")" >> $model
	echo "lr.linear_regression($w_b_tuple)" >> $model
	i=$(($i+1))
done
