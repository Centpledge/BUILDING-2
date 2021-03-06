
// Some data omitted for clarity on screen!
var data = [{
  name: "Asia",
  text: ["Afghanistan", "Bahrain", "Bangladesh", ..., "Yemen, Rep."],
  marker: {
    sizemode: "area",
    sizeref: 200000,
    size : [31889923, 708573, 150448339, ..., 22211743]
  },
  mode: "markers",
  y: [974.5803384, 29796.04834, 1391.253792, ..., 2280.769906],
  x: [43.828, 75.635, 64.062, ..., 62.698],
  uid: "99da6d"
},{
  name:"Europe",
  text: ["Albania", "Austria", "Belgium", ..., "United Kingdom"],
  marker: {
    sizemode: "area",
    sizeref: 200000,
    size: [3600523, 8199783, 10392226, ..., 60776238]
  },
  mode: "markers",
  y: [5937.029526, 36126.4927, 33692.60508, ..., 33203.26128],
  x: [76.423, 79.829, 79.441, ..., 79.425],
  uid: "9d3ba4"
},{
  // more continent data
},
{
  name: "Oceania",
  text: ["Australia","New Zealand"],
  marker: {
    sizemode: "area",
    sizeref: 200000,
    size: [20434176, 4115771]
  },
  mode: "markers",
  y: [34435.36744, 25185.00911],
  x: [81.235, 80.204],
  uid: "f9fb74"
};

var layout = {
  xaxis: {
    title: 'Life Expectancy'
  },
  yaxis: {
    title: 'GDP per Capita',
    type: 'log'
  },
  margin: {
    t: 20
  },
  hovermode: 'closest'
};

Plotly.plot('my-graph', data, layout);
Copied!