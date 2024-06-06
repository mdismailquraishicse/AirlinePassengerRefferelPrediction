from flask import Flask, render_template, request, Response
import numpy as np
from prediction import pred
app = Flask('__name__')



@app.route('/')
def fun():
	result = ''
	return render_template('index.html',
						result = result)

@app.route('/pred', methods=['POST',"GET"])
def prediction():
	cabins = {'economy':0, 'business':0, 'premium economy':0, 'first class':0}
	columns = ['overall', 'seat_comfort', 'cabin_service', 'food_bev', 'value_for_money', 'cabin']
	x = []
	for i in columns:
		x.append(request.form[i])
	for i in cabins.keys():
		if i == x[-1].split()[0].lower():
			cabins[i] = 1
	x = x[:-1]
	cabv = list(cabins.values())
	x.extend(cabv)
	x = np.array(x)
	result = pred(x)
	if result == 0:
		result = "Don't Recommend"
	elif result == 1:
		result = "Recommend"
	return render_template('index.html',
						result = result)

if __name__ == '__main__':
	Flask.run(debug=True)