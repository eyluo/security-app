var obj = {{location_dict|tojson}};
var table_data = '<table><tbody>';

for (var i = 0; i < Object.keys(obj).length; i++) {
  var ip = Object.keys(obj)[i];
  table_data += '<tr>';
  table_data += '<td>' + obj[ip].continent + '</td>';
  table_data += '<td>' + obj[ip].country + '</td>';
  table_data += '<td>' + obj[ip].coordinates + '</td>';
  table_data += '</tr>';
}

table_data += '</tbody><table>';

document.write(table_data);