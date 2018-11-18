from pandas import read_csv
# from pandas import datetime
from datetime import datetime
from matplotlib import pyplot
from statsmodels.tsa.arima_model import ARIMA
from sklearn.metrics import mean_squared_error

def parser(x):
	return datetime.strptime(x, '%Y-%m')

series = read_csv('monthSeries.csv', header=0, parse_dates=[1], index_col=0, squeeze=True, date_parser=parser)
print(series.head())
X = series.values
print(X)
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
for x in train:
	print(x[1])
history = [float(x[1]) for x in train]
predictions = list()
for t in range(len(test)):
	model = ARIMA(history, order=(5,2,0))
	model_fit = model.fit(disp=0)
	# print(model_fit.summary())
	output = model_fit.forecast()
	yhat = output[0]
	print(yhat)
	predictions.append(yhat)
	obs = test[t]
	print(obs[1])
	history.append(obs[1])
	print('predicted=%f, expected=%f' % (yhat, obs[1]))
print(test[:,1])
error = mean_squared_error(test[:, 1], predictions)
print('Test MSE: %.3f' % error)
# plot
pyplot.plot(list(test[:, 1]))
pyplot.plot(predictions, color='red')
pyplot.show()