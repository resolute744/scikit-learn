from sklearn.linear_model import LinearRegression
hours = [[1], [2], [3], [4], [5]]
marks = [[50], [60], [70], [80], [90]]
model = LinearRegression()
model.fit(hours, marks)
predicted = model.predict([[6]])
print("Hours: ", 6)
print("Predicted Marks: ", predicted[0])
