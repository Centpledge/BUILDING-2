from nvd3 import pieChart
type = 'pieChart'
chart = pieChart(name=type, color_category='category20c', height=450, width=450)
xdata = ["Orange", "Banana", "Pear", "Kiwi", "Apple", "Strawberry", "Pineapple"]
ydata = [3, 4, 0, 1, 5, 7, 3]
extra_serie = {"tooltip": {"y_start": "", "y_end": " cal"}}
chart.add_serie(y=ydata, x=xdata, extra=extra_serie)
chart.buildcontent()
print chart.htmlcontent
