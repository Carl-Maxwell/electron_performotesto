var fs = require('fs');

function grabFiles(base, allFiles) {
  allFiles = allFiles || [];

  fs.readdir(base, function(err, files) {
    if (files && files.length) {
      files.forEach(function(file) {
        fs.stat(base + '/' + file, function(err, stat) {
          if (stat.isDirectory()) {
            grabFiles(base + "/" + file, allFiles);
          } else {
            allFiles.push(base + "/" + file);
          }
        });
      });
    }
  });

  return allFiles;
}

// module.exports = function() { return grabFiles; };

// var x = getFiles('./boopa');
//
// var interval = setInterval(function() {
//   //console.log(x);
//   if (x.length > 4) clearInterval(interval);
// }, 1);
