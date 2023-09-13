#!/usr/bin/node
const fs = require('fs');

const concatFiles = (file1, file2, output) => {
  let concatText = '';

  fs.readFile(file1, 'utf8', (err, data) => {
    if (!err) {
      concatText += data + '\n';
      fs.readFile(file2, 'utf8', (err, data) => {
        if (!err) {
          concatText += data;
          fs.writeFile(output, concatText, 'utf8', (err) => {
            if (err) {
              console.log(err);
            }
          });
        } else {
          console.log(err);
        }
      });
    } else {
      console.log(err);
    }
  });
};

const [, , file1, file2, file3] = process.argv;

if (file1 && file2 && file3) {
  concatFiles(file1, file2, file3);
}
