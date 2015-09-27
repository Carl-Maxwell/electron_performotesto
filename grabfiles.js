var fs = require('fs');

function getFiles(base, allFiles) {
  allFiles = allFiles || [];

  fs.readdir(base, function(err, files) {
    files.forEach(function(file) {
      fs.stat(base + '/' + file, function(err, stat) {
        if (stat.isDirectory()) {
          getFiles(base + "/" + file, allFiles);
        } else {
          allFiles.push(base + "/" + file);
        }
      });
    });
  });

  return allFiles;
}


var x = getFiles('./testfiles/');

var interval = setInterval(function() {
  console.log(x);
  if (x.length > 4) clearInterval(interval);
}, 50);
